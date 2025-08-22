from api_call import call_api
from weather_api import get_weather
import json
import time

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather of the city ",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "Name of the city"},
                    "temperature": {"type": "string", "description": "Current temperature of the city"},
                    "humidity": {"type": "string", "description": "Humidity in the city"},
                    "feels_like": {"type": "string", "description": "How it feels in the city"}
                },
                "required": ["city"]
            }
        }
    }
]


if __name__ == "__main__":
  message = input("You: ")
  input_list = [{"role": "user", "content": message}]
  result = call_api(input_list, tools)

import time, json

for choice in result.choices:
    tool_calls = choice.message.tool_calls
    if tool_calls:
        for tool_call in tool_calls:
            args = json.loads(tool_call.function.arguments)

            tool_result = {"Details": get_weather(args["city"])}

            input_list.append({
            "role": "function",
            "name": tool_call.function.name,
            "content": json.dumps(tool_result)
        })


        final_output = call_api(input_list)
        print("Manjulika: ", final_output.choices[0].message.content)
