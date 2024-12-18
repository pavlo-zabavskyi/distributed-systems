import time
import grpc
import asyncio

from . import messages_pb2, messages_pb2_grpc


class MessagesClient():
    __latest_ping_status: str

    MAX_PING_ATTEMPTS = 3       # Max ping attempts
    MAX_RETRIES = 10            # Max retries from task
    RETRY_TIMEOUT = 60          # Retry Timeout in seconds
    RETRY_DELAY = 2             # Delay between retries in seconds
    DEFAULT_PORT = 50051        # Default Node port

    def __init__(self, host: str):
        self.host = host
        self.server_url = '{}:{}'.format(host, self.DEFAULT_PORT)
        self.__ping_attempts = 0

    def __repr__(self) -> str:
        """
        Returns a string representation of the MessagesClient instance.

        Returns:
            str: A string in the format 'MessagesClient(server_url, latest_ping_status)'.
        """
        return f"MessagesClient(server_url={self.server_url})"

    def is_ping_attempts_reached(self) -> bool:
        return self.__ping_attempts == self.MAX_PING_ATTEMPTS

    def is_alive(self) -> bool:
        return self.__latest_ping_status == messages_pb2.PingStatus.OK

    async def ping(self) -> bool:
        """Sends a ping to the server to check its status."""
        try:
            async with grpc.aio.insecure_channel(self.server_url) as channel:
                stub = messages_pb2_grpc.MessagesStub(channel)

                request = messages_pb2.PingRequest()
                response = await stub.Ping(request)

                return response.status == messages_pb2.PingStatus.OK
        except grpc.aio.AioRpcError as e:
            print(f"Ping failed for {self.server_url}: {e}")
            self.__ping_attempts += 1

            return False

    async def append(self, message):
        attempt = 0
        start_time = time.monotonic()

        while time.monotonic() - start_time < self.RETRY_TIMEOUT:
            try:
                response = await self.__try_to_append(message)

                return response
            except grpc.aio.AioRpcError as e:
                print(f"gRPC Error on attempt {attempt + 1}: {e}")
            except Exception as e:
                print(f"Error on attempt {attempt + 1}: {e}")

            attempt += 1
            print(f"Retrying to append {message} message... ({attempt}/{self.MAX_RETRIES})")
            await asyncio.sleep(self.RETRY_DELAY)

        print("All retries failed.")
        raise Exception(f"Failed to append {message} message after {self.MAX_RETRIES} attempts")

    async def __try_to_append(self, message):
        async with grpc.aio.insecure_channel(self.server_url) as channel:
            stub = messages_pb2_grpc.MessagesStub(channel)

            request = messages_pb2.AppendRequest(
                id=message.id,
                message=message.message,
            )
            response = await stub.Append(request)

            return response
