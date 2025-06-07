import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate(text: str, source: str = "kn", target: str = "en") -> str:
    """
    Uses GPT to translate between Kannada and English.
    """
    prompt = f"Translate the following text from {source} to {target}:
{text}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
