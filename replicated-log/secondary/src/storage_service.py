from typing import List
from src.models.message import Message


class StorageService:
    def __init__(self):
        self.__messages: List[Message] = []
        self.__buffer: List[Message] = []
        self.__latest_message_id: int = 0

    @property
    def latest_message_id(self) -> int:
        return self.__latest_message_id

    def append_message(self, message: Message) -> None:
        # print('Log:', self.__latest_message_id, message.id, self.__messages, self.__buffer)

        if message.id == self.__latest_message_id + 1:
            # If the message ID is the next one, add it to __messages
            self.__messages.append(message)
            self.__latest_message_id += 1
            print(f'Message with {message.id} id added to __messages.')

            # Now, check the buffer for any messages that can be added in order
            self.__check_buffer()

        else:
            self.__insert_sorted(message)
            print(f'Message with {message.id} id added to __buffer.')

    def append_messages(self, messages: List[Message]) -> None:
        message_to_append = [Message(message['id'], message['message']) for message in messages]
        self.__messages.extend(message_to_append)
        self.__latest_message_id = self.__messages[-1].id
        self.__check_buffer()

    def get_messages(self) -> List[Message]:
        # print('Reading messages: ', self.__messages)
        return self.__messages

    # private helpers
    def __check_buffer(self):
        # print("Buffer: ", self.__buffer)
        while self.__buffer and self.__buffer[0].id == self.__latest_message_id + 1:
            # The first message in the buffer should be the next one in the sequence
            message = self.__buffer.pop(0)
            self.__messages.append(message)
            self.__latest_message_id += 1
            print(f'Message with {message.id} id moved from buffer to __messages.')

    # TODO: optimize it, use algorithms
    def __insert_sorted(self, message: Message):
        # Check if a message with the same ID already exists
        if any(m.id == message.id for m in self.__buffer):
            return

        index = 0
        while index < len(self.__buffer) and self.__buffer[index].id < message.id:
            index += 1

        self.__buffer.insert(index, message)
