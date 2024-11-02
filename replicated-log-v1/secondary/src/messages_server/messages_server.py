import asyncio
import random
import grpc
from . import messages_pb2, messages_pb2_grpc


class MessagesServicer(messages_pb2_grpc.MessagesServicer):
    def __init__(self, storage):
        self.storage = storage

    async def Append(
        self,
        request: messages_pb2.AppendRequest,
        context: grpc.aio.ServicerContext,
    ) -> messages_pb2.AppendResponse:
        delay = random.randint(1, 10)
        print(f'[Secondary] Going to save "{request.message}" message with {delay} sec delay...')
        await asyncio.sleep(delay)

        await self.storage.append(request.message)
        return messages_pb2.AppendResponse(status='success')

    async def GetAllMessages(
            self,
            request: messages_pb2.GetAllMessagesRequest,
            context: grpc.aio.ServicerContext,
    ) -> messages_pb2.GetAllMessagesResponse:
        print('[Secondary] Retrieving all messages...')
        messages = await self.storage.get_messages()
        return messages_pb2.GetAllMessagesResponse(messages=messages)


async def serve(storage) -> None:
    server = grpc.aio.server()
    messages_pb2_grpc.add_MessagesServicer_to_server(MessagesServicer(storage), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()
