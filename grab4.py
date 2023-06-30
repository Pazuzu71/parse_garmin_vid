import aiofiles
import os
from aiohttp import ClientSession
import asyncio
from fake_useragent import UserAgent
import time


async def generate_urls():
    urls = []
    for k in range(1, 2):
        for i in range(30):
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


async def fetch_status(url: str):
    ua = UserAgent()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }
    async with ClientSession() as session:
        async with session.get(url=url, headers=headers) as result:
            file_name = url.split(r'/')[-1]
            if result.status == 200:
                async with aiofiles.open(f'temp_async\\{file_name}', 'wb') as handle:
                    while True:
                        chunk = await result.content.read(1024)
                        if not chunk:
                            break
                        await handle.write(chunk)


async def main():

    if not os.path.exists('temp'):
        os.mkdir('temp')
    if not os.path.exists('temp_async'):
        os.mkdir('temp_async')

    generated_urls = await generate_urls()
    requests = [fetch_status(url) for url in generated_urls]
    await asyncio.gather(*requests)
    time.sleep(1)


asyncio.run(main())
