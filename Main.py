from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from DataAPI import chatBot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
     allow_origins=[
        "http://localhost:5173",
        "https://bisto-bos.web.app"
    ],
    allow_credentials=True,
     allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"response": "Hello, World!"}

@app.post("/chat")
def chat(request :ChatRequest):
    answer = chatBot(request.question)
    return {
        'question': request.question,
        "answer": answer
    }



    