def generate_alert(flag):
    prompt = f"""
A business issue has been detected:

{flag}

Write a short alert (max 2 sentences).
Include:
- the problem
- one immediate action
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content
