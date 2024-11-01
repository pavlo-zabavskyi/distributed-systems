import asyncio
from fastapi import FastAPI
from models.message import MessageRequest
from config import storage, secondaryClients

app = FastAPI()


@app.post('/append')
async def append(message_request: MessageRequest):
    message = message_request.message
    print(f'[Master] Going to save "{message}" message...')

    await storage.append(message)

    try:
        await asyncio.gather(
            *[client.append(message) for client in secondaryClients]
        )
        print('Successfully appended message to all secondary clients.')
    except Exception as e:
        print(f'Error while appending message to secondary clients: {e}')

    return {
        "status": "success"
    }


@app.get('/messages')
async def msgs_list():
    messages = await storage.get_messages()

    return {
        "status": "success",
        "messages": messages
    }
