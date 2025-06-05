from src.chatbot.graph import create_workflow
import time

def chat():
    print("Cohere Chatbot: Hello! How can I help you today? (Type 'quit' to exit)\n")
    app = create_workflow()

    # Initialize state with an empty conversation or a welcome message
    state = {"messages": [{"role": "assistant", "content": "Hello! How can I help you today?"}]}
    print(f"Chatbot: {state['messages'][-1]['content']}\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
                print("Chatbot: Goodbye! It was nice talking to you.")
                break
            
            if not user_input:
                print("Chatbot: Please type something meaningful.")
                continue
            
            # Append user message
            state["messages"].append({"role": "user", "content": user_input})

            print("\nChatbot is thinking...", end="", flush=True)
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print("\n")

            # Invoke graph once per user message (one step)
            state = app.invoke(state)

            # Output the assistant's latest response
            print(f"Chatbot: {state['messages'][-1]['content']}\n")

        except Exception as e:
            print(f"Chatbot: Sorry, I encountered an error: {e}")
            print("Let's start a new conversation.\n")
            # Reset state to start fresh
            state = {"messages": [{"role": "assistant", "content": "Let's try again. How can I help you?"}]}

if __name__ == "__main__":
    chat()
