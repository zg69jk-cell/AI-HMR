import os
import streamlit
from dotenv import load_dotenv
from openai import OpenAI

from rules import evaluate_business
from prompts import SYSTEM_PROMPT, build_user_prompt

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_business(data):
    # Step 1: Run rules
    flags = evaluate_business(data)

    # Step 2: Sort by severity
    flags = sorted(flags, key=lambda x: x["severity"], reverse=True)

    # Step 3: Build prompt
    user_prompt = build_user_prompt(data, flags)

    # Step 4: Call OpenAI
    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # fast + cheap for MVP
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    # Example input data
    business_data = {
        "this_week_sales": 8000,
        "last_week_sales": 10000,
        "expenses": 5000,
        "avg_expenses": 3500,
        "inventory_days": 52,
        "owner_approvals_pct": 75,
        "top_bonus": 12,
        "avg_bonus": 8,
        "business_type": "retail clothing",
        "num_employees": 6
    }

    result = analyze_business(business_data)
    print("\n=== AI BUSINESS REPORT ===\n")
    print(result)
