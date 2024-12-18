import asyncio
import random
import grpc

from . import messages_pb2, messages_pb2_grpc
from ..models.message import Message


class MessagesServicer(messages_pb2_grpc.MessagesServicer):
    def __init__(self, storage):
        self.storage = storage

    def Ping(self, request, context) -> messages_pb2.PingResponse:
        return messages_pb2.PingResponse(status=messages_pb2.PingStatus.OK)

    async def Append(
        self,
        request: messages_pb2.AppendRequest,
        context: grpc.aio.ServicerContext,
    ) -> messages_pb2.AppendResponse:
        delay = random.randint(1, 10)
        print(f'[Secondary] Going to save "{request.message}" message with {delay} sec delay...')
        await asyncio.sleep(delay)

        message_to_append = Message(request.id, request.message)
        self.storage.append_message(message_to_append)

        return messages_pb2.AppendResponse(status='success')

    def GetAllMessages(
            self,
            request: messages_pb2.GetAllMessagesRequest,
            context: grpc.aio.ServicerContext,
    ) -> messages_pb2.GetAllMessagesResponse:
        print('[Secondary] Retrieving all messages...')
        messages = self.storage.get_messages()

        response_messages = []
        for message in messages:
            response_message = messages_pb2.MessageResponse(
                id=message.id,
                message=message.message,
            )
            response_messages.append(response_message)

        return messages_pb2.GetAllMessagesResponse(messages=response_messages)


async def serve(storage) -> None:
    print('Starting Messages gRPC server...')
    server = grpc.aio.server()
    messages_pb2_grpc.add_MessagesServicer_to_server(MessagesServicer(storage), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()
