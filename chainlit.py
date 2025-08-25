import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
        # Your logic goes here
        # For now, we'll just send back a message

        # Send a response back to the user
        await cl.Message(
            content=f"You said: {message.content}",
        ).send()