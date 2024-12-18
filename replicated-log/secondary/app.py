import asyncio
from src.join_node import join_node
from src.messages_server.messages_server import serve
from src.config import storage


async def main():
    """Run messages gRPC server and join node concurrently."""
    await join_node()
    await serve(storage)


if __name__ == '__main__':
    asyncio.run(main())
