from typing import List, Any
from models.message import Message


# Additional logic with messages ordering is implemented on "secondary" node storage
class StorageService:
    """
    A service to store and manage messages.

    Attributes:
        __messages (List[Message]): A private list that holds all stored messages.
        __latest_message_id (int): A private counter that tracks the ID of the latest message.
    """

    def __init__(self):
        """
        Initializes the StorageService with an empty list of messages
        and sets the latest message ID to 1.
        """
        self.__messages: List[Message] = []
        self.__latest_message_id: int = 0

    @property
    def latest_message_id(self) -> int:
        """
        Returns:
            int: The ID of the latest message.
        """
        return self.__latest_message_id

    async def append(self, message: Message) -> None:
        """
        Appends a new message to the storage and increments the message ID.

        Args:
            message (Message): The message to be stored.
        """
        self.__messages.append(message)
        self.__latest_message_id += 1

    async def get_messages(self) -> List[Message]:
        """
        Retrieves all stored messages.

        Returns:
            List[Any]: A list of all messages in storage.
        """
        return self.__messages
