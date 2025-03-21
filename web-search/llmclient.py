from ollama import chat
from ollama import ChatResponse


def get_response(message: str) -> str:
    response: ChatResponse = chat(
        model="deepseek-r1:1.5b",
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return response["message"]["content"]
