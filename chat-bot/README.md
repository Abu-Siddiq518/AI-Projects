python Local CLI Chatbot

This project implements a simple command-line chatbot in Python using a small Hugging Face text generation model. It maintains conversation history with a sliding window to provide contextually relevant responses.

## Features

*   Uses a Hugging Face text generation model for responses.
*   Maintains conversation history using a sliding window.
*   Provides a simple command-line interface for interaction.

## Setup

1.  **Clone the repository (if applicable) or download the project files.**
2.  **Install the required libraries:**
    ```bash
    # Create a virtual environment named .venv
    python -m venv .venv

    source .venv/bin/activate
    pip install transformers torch
    ```
3.  **Ensure you have a CUDA-enabled GPU** if you want to leverage GPU acceleration (recommended for better performance).

## How to Run

1.  **Navigate to the project directory** in your terminal.
2.  **Run the main interface script:**
    ```bash
    python interface.py
    ```
3.  The chatbot will load the model and prompt you to start chatting.

## Sample Interaction

```
Loading model...
Model loaded successfully.
Start chatting (type 'quit' or 'exit' to stop):
You: Hello!
Bot: Hello there! How can I help you today?
You: What is the capital of France?
Bot: The capital of France is Paris.
You: Thank you!
Bot: You're welcome! Is there anything else I can assist you with?
You: exit
Exiting chatbot.
```

## Files

*   `model_loader.py`: Handles loading the Hugging Face model and tokenizer.
*   `chat_memory.py`: Implements the sliding window memory buffer for conversation history.
*   `interface.py`: Provides the command-line interface and integrates the other components.
*   `README.md`: This file, providing project information and instructions.

  ## Sample Output
<img width="1915" height="1079" alt="Screenshot 2025-08-22 194945" src="https://github.com/user-attachments/assets/fe671bf0-6f08-4223-86ce-db6efa58b7df" />

  
