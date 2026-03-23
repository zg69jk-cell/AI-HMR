import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import SYSTEM_PROMPT, build_user_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_ai_report(data, flags):
    prompt = build_user_prompt(data, flags)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
