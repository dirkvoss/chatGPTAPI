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

prompt = "ich brauche ein iobroker javascript das konitnierlich die Variable alias.0.Strom.aktSpeicherBeladung_Watt überwacht. Wenn diese negativ wird  soll die Variable awtrix-light.0.apps.speicherentladen.visible  auf True  und awtrix-light.0.apps.speicherladen.visible auf false gesetzt werden. Wenn sie aber positiv  oder 0 wird soll die Variable awtrix-light.0.apps.speicherentladen.visible  auf False und awtrix-light.0.apps.speicherladen.visible auf True gesetzt werden."

response = get_completion(prompt)

print(response)