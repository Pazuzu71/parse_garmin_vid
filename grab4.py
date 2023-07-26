import aiofiles
import os
from aiohttp import ClientSession
import asyncio
from fake_useragent import UserAgent
import time


async def generate_urls():
    urls = []
    for k in range(1, 5):
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


async def fetch_status(semaphore1, semaphore2, url: str):
    ua = UserAgent()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }
    async with semaphore1:
        async with ClientSession() as session:
            async with session.get(url=url, headers=headers) as result:
                file_name = url.split(r'/')[-1]
                if result.status == 200:
                    async with semaphore2:
                        async with aiofiles.open(f'temp_async2//{file_name}', 'wb') as handle:
                            while True:
                                chunk = await result.content.read(1024)
                                if not chunk:
                                    break
                                await handle.write(chunk)


async def main():

    if not os.path.exists('temp'):
        os.mkdir('temp')
    if not os.path.exists('temp_async2'):
        os.mkdir('temp_async2')
    semaphore1 = asyncio.Semaphore(3)
    semaphore2 = asyncio.Semaphore(3)
    generated_urls = await generate_urls()
    requests = [fetch_status(semaphore1, semaphore2, url) for url in generated_urls]
    await asyncio.gather(*requests)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
