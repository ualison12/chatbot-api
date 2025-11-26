from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

# Pegando a chave da OpenAI do ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# Liberar CORS para qualquer site seu
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo da mensagem recebida do front-end
class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(data: Message):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=data.message
    )

    return {
        "reply": response.output_text
    }

