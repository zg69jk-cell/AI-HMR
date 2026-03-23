import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_model(messages, temperature=0.4):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content
