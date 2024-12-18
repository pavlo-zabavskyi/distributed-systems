from storage_service import StorageService
from replication_manager import ReplicationManager

storage = StorageService()

replication_manager = ReplicationManager()
replication_manager.start_heartbeat()
