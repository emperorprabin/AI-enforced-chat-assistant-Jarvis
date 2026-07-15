import os
from google import genai
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # required by the library, but ignored locally
)

response = client.chat.completions.create(
    model="mistral",
    messages=[
        {"role": "system", "content": "You are a helpful assistant chatbot like siri or alxa. Give clear and short answers."},
        {"role": "user", "content": "command"}
    ]
)

print(response.choices[0].message.content)