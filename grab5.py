import aiohttp
import asyncio
import aiofiles


async def download_file(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            async with aiofiles.open(filename, 'wb') as file:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    await file.write(chunk)


async def main():
    url = 'https://connectvideo.garmin.com/msn-workout/Strength/S_147-A3.mp4'
    filename = 'S_147-A3.mp4'
    await download_file(url, filename)
    print("Файл успешно скачан")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
