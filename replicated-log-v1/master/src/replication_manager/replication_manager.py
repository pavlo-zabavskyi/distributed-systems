import asyncio


class ReplicationManager:
    TIMEOUT = 60000

    def __init__(self, secondaries):
        self.secondaries = secondaries

    async def replicate_message(self, message, write_concern):
        tasks = [asyncio.create_task(client.append(message)) for client in self.secondaries]
        loop = asyncio.get_running_loop()

        return await self._execute_tasks(tasks, loop, write_concern)

    async def _execute_tasks(self, tasks, loop, return_when):
        """Internal helper for replicate_message()."""

        waiter = loop.create_future()
        counter = 0
        timeout_handle = loop.call_later(self.TIMEOUT, self._release_waiter, waiter)

        def _on_completion(task):
            nonlocal counter
            counter += 1
            if (counter >= return_when or counter == len(tasks) and
                    (not task.cancelled() and task.exception() is not None)):
                timeout_handle.cancel()
                if not waiter.done():
                    waiter.set_result(None)

        for task in tasks:
            task.add_done_callback(_on_completion)


        done, pending = set(), set()
        try:
            if return_when == 0:
                waiter
                return done, pending
            else:
                await waiter
        finally:
            timeout_handle.cancel()
            for task in tasks:
                task.remove_done_callback(_on_completion)

        for task in tasks:
            if task.done():
                done.add(task)
            else:
                pending.add(task)

        return done, pending

    def _release_waiter(self, waiter):
        if not waiter.done():
            waiter.set_result(None)
