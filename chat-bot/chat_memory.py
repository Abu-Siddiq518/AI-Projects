
class ChatMemory:
    """Implements a sliding window memory buffer for conversation history."""

    def __init__(self, max_size: int = 10):
        """Initializes the ChatMemory with an empty message list and a maximum size.

        Args:
            max_size: The maximum number of messages to store in the buffer.
                      Defaults to 10.
        """
        self.messages = []
        self.max_size = max_size

    def add_message(self, message: dict):
        """Adds a message to the memory buffer.

        If the buffer size exceeds max_size, the oldest message(s) are removed.

        Args:
            message: A dictionary representing the message (e.g., {'role': 'user', 'content': '...'}).
        """
        self.messages.append(message)
        if len(self.messages) > self.max_size:
            # Remove oldest messages to maintain the sliding window
            self.messages = self.messages[-self.max_size:]

    def get_messages(self) -> list:
        """Returns the current list of messages in the memory buffer."""
        return self.messages

    def clear(self):
        """Clears the memory buffer, removing all messages."""
        self.messages = []
