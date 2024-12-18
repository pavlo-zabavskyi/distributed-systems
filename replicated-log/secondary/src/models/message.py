class Message:
    """
    Represents a message with an identifier, content, and creation timestamp.

    Attributes:
        id (int): The unique identifier for the message.
        message (str): The content of the message.
    """

    def __init__(self, id: int, message: str):
        """
        Initializes a new Message instance.

        Args:
            id (int): The unique identifier for the message.
            message (str): The content of the message.
        """
        self.id = id
        self.message = message

    def __repr__(self) -> str:
        """
        Returns a string representation of the Message instance.

        Returns:
            str: A string in the format 'Message(id, message, created_at)'.
        """
        return f"Message(id={self.id}, message='{self.message}')"

    def to_dict(self) -> dict:
        """
        Converts the Message instance into a dictionary.

        Returns:
            dict: A dictionary containing the message's attributes.
        """
        return {
            "id": self.id,
            "message": self.message,
        }
