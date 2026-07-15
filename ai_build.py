import os
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JuFuv731lf4OWvqAPKrlh-9Wsx8heHF0s4zV4vf7ptRw")

response = client.models.generate_content(
    model="gemini-2.5-flash",  # fast + free-tier friendly
    contents="Write a one-sentence bedtime story about a unicorn."
)

print(response.text)