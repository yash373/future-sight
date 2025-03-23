from ollama import chat
from ollama import ChatResponse


def get_response(message: str) -> str:
    response: ChatResponse = chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return response["message"]["content"]
