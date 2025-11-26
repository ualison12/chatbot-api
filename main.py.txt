from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from chatbot_engine import Chatbot

app = FastAPI(title="Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bot = Chatbot(nome="UaliBot")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def root():
    return {"message": "API do Chatbot está no ar 🚀"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    resposta = bot.responder(request.message)
    return ChatResponse(reply=resposta)
