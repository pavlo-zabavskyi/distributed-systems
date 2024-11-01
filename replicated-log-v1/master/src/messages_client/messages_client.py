import grpc

from . import messages_pb2, messages_pb2_grpc


class MessagesClient():
    def __init__(self, host, server_port):
        self.host = host
        self.server_port = server_port

    async def append(self, message):
        async with grpc.aio.insecure_channel('{}:{}'.format(self.host, self.server_port)) as channel:
            stub = messages_pb2_grpc.MessagesStub(channel)
            request = messages_pb2.AppendRequest(message=message)
            response = await stub.Append(request)

            return response
