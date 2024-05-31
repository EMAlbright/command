from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv('APIKEY')
client = OpenAI(api_key=key)

userInput = input("Enter a prompt: ")


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
