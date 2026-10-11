from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

app = FastAPI(title="News Agent API")

model = ChatGroq(model="openai/gpt-oss-120b")
search_tool = DuckDuckGoSearchRun()

agent = create_agent(
    model=model,
    tools=[search_tool],
    system_prompt=(
        "You are a helpful news assistant. Search for current information "
        "when needed. Summarize findings clearly and mention dates when available."
    ),
)


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "News Agent API is running"}


@app.post("/ask")
def ask_question(data: Question):
    try:
        response = agent.invoke({
            "messages": [{"role": "user", "content": data.question}]
        })
        answer = response["messages"][-1].content
        if not isinstance(answer, str):
            answer = str(answer)
        return {"answer": answer}
    except Exception as exc:
        raise HTTPException(status_code=500, detail="The agent request failed. Check backend logs and API configuration.") from exc
