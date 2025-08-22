from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def call_api(messages,tools=None):
    completion = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
      "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="openai/gpt-3.5-turbo-0613",
    tools=tools,
    temperature = 0.8,
    messages= messages
  )
    return completion

if __name__ == "__main__":

    ques = input("How can I assist you today?\n")
    result = call_api(ques)

    print(result)
