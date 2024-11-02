from storage.storage_service import StorageService
from messages_client.messages_client import MessagesClient
from replication_manager.replication_manager import ReplicationManager

storage = StorageService()

secondary_clients = [
    MessagesClient('secondary-a', '50051'),
    MessagesClient('secondary-b', '50051'),
    MessagesClient('secondary-c', '50051')
]

replication_manager = ReplicationManager(secondary_clients)
