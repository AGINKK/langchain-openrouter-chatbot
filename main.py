
from langchain_openrouter import ChatOpenRouter

chat_model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0.7
)

messages = [
    ("system", "You are a helpful chatbot. Answer in simple English.")
]

print("Chatbot started!")
print("Type 'exit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    messages.append(("human", user_input))

    try:
        response = chat_model.invoke(messages)
        print("Bot:", response.content)
        messages.append(("ai", response.content))

    except Exception as error:
        print("An error occurred:", error)