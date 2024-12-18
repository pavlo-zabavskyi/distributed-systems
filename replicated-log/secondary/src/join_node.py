from typing import List
from src.helpers.http_request import get, post
from src.config import storage
from src.models.message import Message

MASTER_URL = "http://master_node:8050"  # should be the same as master node container name


async def get_messages_from_master(starting_message_id: int) -> List[Message]:
    query_params = {
        "startingMessageId": starting_message_id
    }
    messages = await get(f"{MASTER_URL}/messages", query_params)

    return messages["messages"]


async def join_node() -> None:
    print('Joining to Master node...')
    latest_saved_message_id = storage.latest_message_id

    print(f'Fetching Messages from Master node from {latest_saved_message_id + 1} message...')
    messages = await get_messages_from_master(latest_saved_message_id + 1)
    print(f'Fetching Messages from Master node successfully finished. Copied {len(messages)} messages.')

    storage.append_messages(messages)

    await post(f"{MASTER_URL}/join_node")
    print('Joining to Master node successfully finished.')
