import asyncio

from src.storage.storage_service import StorageService
from src.messages_server.messages_server import serve


def main():
    """Run messages gRPC server."""
    print('Starting Messages gRPC server...')
    storage = StorageService()
    asyncio.run(serve(storage))


if __name__ == '__main__':
    main()
