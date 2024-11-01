import aiofiles


class StorageService:
    __filename = 'messages.csv'

    def __init__(self):
        with open(self.__filename, 'w') as f:
            pass

    async def append(self, message):
        async with aiofiles.open(self.__filename, 'a') as f:
            await f.write(message + '\n')

    async def get_messages(self):
        try:
            # Asynchronously open file for reading
            async with aiofiles.open(self.__filename, 'r') as f:
                content = await f.read()
                lines = [line for line in content.split('\n') if line]

                return lines

        except FileNotFoundError:
            return "File not found."
