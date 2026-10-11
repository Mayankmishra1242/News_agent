# News Research Assistant (LangChain + FastAPI + Streamlit)

A starter project with a LangChain agent that can search the web using DuckDuckGo, a FastAPI backend, and a Streamlit chat UI.

## Project structure

```text
news-agent/
├── backend/
│   ├── __init__.py
│   └── main.py
├── frontend/
│   └── app.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10+
- A Groq API key

## Setup

### 1. Create and activate a virtual environment

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure the API key

Copy `.env.example` to `.env` and replace the placeholder with your own Groq API key.

macOS/Linux:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Never commit or share your real `.env` file.

### 4. Start FastAPI

Run from the project root:

```bash
uvicorn backend.main:app --reload
```

Check the API at http://127.0.0.1:8000/ and test it at http://127.0.0.1:8000/docs.

### 5. Start Streamlit in a second terminal

Activate the same virtual environment, then run from the project root:

```bash
streamlit run frontend/app.py
```

## How it works

1. Streamlit collects a user question.
2. Streamlit sends a POST request to FastAPI's `/ask` endpoint.
3. FastAPI invokes the LangChain agent.
4. The agent can call DuckDuckGo search.
5. FastAPI returns the final answer to Streamlit.

## API example

Request:

```json
{
  "question": "Protests in Delhi today?"
}
```

Endpoint: `POST http://127.0.0.1:8000/ask`

Response shape:

```json
{
  "answer": "..."
}
```

## Notes

- This starter returns a complete answer; it does not stream tokens to the UI.
- Search results may be incomplete or stale. Verify important news against reliable sources.
- Add authentication, rate limiting, logging, and stronger error handling before exposing the API publicly.
