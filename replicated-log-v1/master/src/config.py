from storage.storage_service import StorageService
from messages_client.messages_client import MessagesClient

storage = StorageService()

secondaryClients = [
    MessagesClient('secondary-a', '50051'),
    MessagesClient('secondary-b', '50051'),
    MessagesClient('secondary-c', '50051')
]
