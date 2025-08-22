import sys
from model_loader import load_model
from chat_memory import ChatMemory

def run_chatbot(model_name: str = "Qwen/Qwen3-0.6B", memory_size: int = 10):
    """Runs the command-line chatbot.

    Args:
        model_name: The name of the Hugging Face model to use.
        memory_size: The maximum number of messages to keep in memory.
    """
    print("Loading model...")
    try:
        pipe = load_model(model_name)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

    chat_memory = ChatMemory(max_size=memory_size)

    print("Start chatting (type 'quit' or 'exit' to stop):")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit']:
            print("Exiting chatbot.")
            break

        user_message = {"role": "user", "content": user_input}
        chat_memory.add_message(user_message)

        messages = chat_memory.get_messages()

        try:
            # The pipeline expects a list of message dictionaries
            # The output is a list containing one dictionary with 'generated_text'
            # which is a list of message dictionaries including the assistant's response
            response = pipe(messages)
            if response and isinstance(response, list) and response[0].get('generated_text'):
                 # Find the last message which should be the assistant's response
                assistant_message = next((msg for msg in reversed(response[0]['generated_text']) if msg.get('role') == 'assistant'), None)

                if assistant_message:
                    assistant_response_content = assistant_message.get('content', '').strip()
                    print(f"Bot: {assistant_response_content}")
                    bot_message = {"role": "assistant", "content": assistant_response_content}
                    chat_memory.add_message(bot_message)
                else:
                     print("Bot: Could not extract assistant's response.")

            else:
                print("Bot: Could not generate a response.")

        except Exception as e:
            print(f"Error during response generation: {e}")
            # Optionally, you might want to remove the last user message if generation fails
            # chat_memory.messages.pop()


if __name__ == "__main__":
    run_chatbot()
