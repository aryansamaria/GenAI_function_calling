from test import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def call_api(ques):
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
    result = call_api(ques)

    print(result)

