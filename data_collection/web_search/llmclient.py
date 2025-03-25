from ollama import chat
from ollama import ChatResponse
from ollama import embeddings

# Normal Models
def get_response(message: str) -> str:
    response: ChatResponse = chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return response["message"]["content"]

# Embedded Models Testing
# def get_response(message: str) -> str:
#     response = embeddings(model='nomic-embed-text', prompt=message)
#     return response
