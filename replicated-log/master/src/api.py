from fastapi import FastAPI, Request, HTTPException
from models.message_request import MessageRequest
from models.message import Message
from config import storage, replication_manager

app = FastAPI()


@app.post('/append')
async def append(message_request: MessageRequest):
    if not replication_manager.is_quorum_reached:
        raise HTTPException(
            status_code=503,
            detail="Replication is not enabled due to insufficient quorum. Read mode is only available."
        )

    write_concern = message_request.write_concern
    message = Message(
        storage.latest_message_id + 1,
        message_request.message,
    )

    print(f'[Master] Going to save "{message}" message with write concern {write_concern}...')

    await storage.append(message)
    await replication_manager.replicate_message(message, write_concern - 1)

    return {"status": "success"}


@app.post('/join_node')
async def join_node(request: Request):
    node_host = request.client.host
    replication_manager.add_secondary(node_host)

    return {"status": "success"}


@app.get('/messages')
async def msgs_list():
    messages = await storage.get_messages()

    return {
        "status": "success",
        "messages": messages
    }
