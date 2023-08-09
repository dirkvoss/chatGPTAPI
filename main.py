import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
        )
    return response.choices[0].message["content"]

# read prompt from keyboard as string
prompt = input("Frage eingeben: ")

response = get_completion(prompt)

print(response)