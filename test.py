from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

def call_api(user_input):
  messages = [
    {"role": "user", "content": user_input}
  ]

  completion = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": "https://yoursite.com",
      "X-Title": "Your App Name",
    },
    model="openai/o1-mini",
    messages=messages,
    max_tokens=5000,
  )
  return completion.choices[0].message.content

def call_web_search(ques):
  completion = client.chat.completions.create(
    model="openai/o4-mini",
    web_search_options={},
    messages=[
      {
        "role": "user",
        "content": ques,
      }
    ],
    max_tokens=5000,
  )
  return completion.choices[0].message.content

if __name__ == "__main__":
  ques = input("How can I assist you today?\n")

  result_of_normal_call = call_api(ques)
  print("Output of normal call")
  print(result_of_normal_call)

  result_of_web_search = call_web_search(ques)
  print("Output of web search call")
  print(result_of_web_search)
