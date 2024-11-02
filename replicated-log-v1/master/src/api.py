from fastapi import FastAPI
from models.message import MessageRequest
from config import storage, replication_manager

app = FastAPI()


@app.post('/append')
async def append(message_request: MessageRequest):
    message = message_request.message
    write_concern = message_request.write_concern

    print(f'[Master] Going to save "{message}" message with write concern {write_concern}...')

    await storage.append(message)
    await replication_manager.replicate_message(message, write_concern-1)

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
