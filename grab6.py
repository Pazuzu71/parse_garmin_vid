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

async def download_multiple_files(file_urls):
    tasks = []
    for url, filename in file_urls.items():
        tasks.append(download_file(url, filename))
    await asyncio.gather(*tasks)

async def main():
    file_urls = {
        'https://connectvideo.garmin.com/msn-workout/Strength/S_002-C1.mp4': 'S_002-C1.mp4',
        'https://connectvideo.garmin.com/msn-workout/Strength/S_004-A1.mp4': 'S_004-A1.mp4',
        'https://connectvideo.garmin.com/msn-workout/Strength/S_004-B1.mp4': 'S_004-B1.mp4'
    }
    await download_multiple_files(file_urls)
    print("Все файлы успешно скачаны")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
