import asyncio
from typing import Set, Tuple, List
from models.message import Message
from messages_client.messages_client import MessagesClient


class ReplicationManager:
    TIMEOUT = 20 * 1000     # Timeout in milliseconds
    HEARTBEAT_INTERVAL = 3  # Heartbeat interval in seconds
    QUORUM = 1              # Min number of active replica nodes

    def __init__(self):
        self.__secondaries: List[MessagesClient] = []
        self._stop_heartbeat = asyncio.Event()

    @property
    def active_replica_nodes(self) -> List[MessagesClient]:
        return list(filter(lambda n: n.is_alive, self.__secondaries))

    @property
    def number_of_active_replica_nodes(self) -> int:
        return len(self.active_replica_nodes)

    @property
    def is_quorum_reached(self) -> bool:
        return self.number_of_active_replica_nodes >= self.QUORUM

    async def replicate_message(self, message: Message, write_concern: int):
        tasks = [asyncio.create_task(client.append(message)) for client in self.active_replica_nodes]

        if write_concern == 0:
            return tasks

        loop = asyncio.get_running_loop()

        return await self._execute_tasks(tasks, loop, write_concern)

    def start_heartbeat(self):
        print("[Heartbeat] Starting heartbeat monitoring...")
        asyncio.create_task(self.__monitor_heartbeats())

    def stop_heartbeat(self):
        print("[Heartbeat] Stopping heartbeat monitoring...")
        self._stop_heartbeat.set()

    def add_secondary(self, secondary_host: str):
        print(f"Adding new secondary node on {secondary_host} host...")

        # Check if a MessagesClient with the same secondary_host already exists
        if any(client.host == secondary_host for client in self.__secondaries):
            print(f"Secondary node with host {secondary_host} already exists.")
            return

        new_secondary = MessagesClient(secondary_host)
        self.__secondaries.append(new_secondary)

    """ Helpers """
    async def _execute_tasks(
            self,
            tasks: list,
            loop: asyncio.AbstractEventLoop,
            return_when: int
    ) -> Tuple[Set[asyncio.Task], Set[asyncio.Task]]:
        waiter = loop.create_future()
        counter = 0
        timeout_handle = loop.call_later(self.TIMEOUT, self._release_waiter, waiter)

        def _on_completion():
            nonlocal counter
            counter += 1
            if counter == len(tasks) or counter >= return_when:
                timeout_handle.cancel()
                if not waiter.done():
                    waiter.set_result(None)

        for task in tasks:
            task.add_done_callback(_on_completion)

        try:
            await waiter
        finally:
            timeout_handle.cancel()
            for task in tasks:
                task.remove_done_callback(_on_completion)

        done, pending = set(), set()
        for task in tasks:
            if task.done():
                done.add(task)
            else:
                pending.add(task)

        return done, pending

    def _release_waiter(self, waiter: asyncio.Future) -> None:
        if not waiter.done():
            waiter.set_result(None)

    async def __monitor_heartbeats(self):
        while not self._stop_heartbeat.is_set():
            for client in self.__secondaries:
                try:
                    is_alive = await client.ping()

                    if not is_alive:
                        print(f"[Heartbeat] Secondary {client} is unreachable.")

                        if client.is_ping_attempts_reached():
                            self.__secondaries.remove(client)

                except Exception as e:
                    print(f"[Heartbeat] Error pinging secondary {client}: {e}")

            await asyncio.sleep(self.HEARTBEAT_INTERVAL)
