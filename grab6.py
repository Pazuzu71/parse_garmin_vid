import aiohttp
import asyncio
import aiofiles


async def generate_urls():
    urls = []
    for k in range(7, 10):
        for i in range(1000):
            for j in "ABCDE":
                if i < 10:
                    num = f'00{i}'
                elif i < 100:
                    num = f'0{i}'
                else:
                    num = str(i)
                file_name = f'S_{num}-{j}{k}.mp4'
                urls.append(f'https://connectvideo.garmin.com/msn-workout/Strength/{file_name}')
    return urls


async def download_file(url, filename, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    async with aiofiles.open(f'temp_async//{filename}', 'wb') as file:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            await file.write(chunk)


async def download_multiple_files(urls):
    tasks = []
    semaphore = asyncio.Semaphore(3)
    file_urls = {x: x.split(r'/')[-1] for x in urls}
    for url, filename in file_urls.items():
        tasks.append(download_file(url, filename, semaphore))
    await asyncio.gather(*tasks)


async def main():
    # file_urls = {
    #     'https://connectvideo.garmin.com/msn-workout/Strength/S_002-C1.mp4': 'S_002-C1.mp4',
    #     'https://connectvideo.garmin.com/msn-workout/Strength/S_004-A1.mp4': 'S_004-A1.mp4',
    #     'https://connectvideo.garmin.com/msn-workout/Strength/S_004-B1.mp4': 'S_004-B1.mp4'
    # }
    urls = await generate_urls()
    await download_multiple_files(urls)
    print("Все файлы успешно скачаны")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
