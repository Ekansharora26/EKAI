import os
from dotenv import load_dotenv

load_dotenv()

def explain_decision(context: str) -> str:
    """
    Generates an AI explanation.
    This function NEVER crashes the app.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    # ✅ If no API key, fail gracefully
    if not api_key:
        return (
            "AI explanation is currently unavailable because no API key is configured. "
            "EKAI’s rule-based decision remains valid."
        )

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a senior software engineer explaining an evaluation decision.

Context:
{context}

Explain the reasoning calmly, professionally, and concisely.
Avoid hype. Be honest and constructive.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You explain engineering decisions clearly."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
            max_tokens=120,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI explanation failed safely: {str(e)}"
