import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv('APIKEY')
client = OpenAI(api_key=key)
r = sr.Recognizer()
engine = pyttsx3.init()
def recordText():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText 
        except sr.RequestError as e:
            print("Could not request results")

def outputText(text):
    with open('output.txt', 'a') as f:
        f.write(text + '\n')

while True:
    text = recordText()
    userInput = text

    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": userInput},
    {"role": "assistant", "content": ""}
  ]

    response  = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
  )

    assistant_response = response.choices[0].message.content
    print("Assistant's response:", assistant_response)
    engine.say(assistant_response)
    engine.runAndWait()