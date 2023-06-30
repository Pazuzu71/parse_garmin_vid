import aiohttp
from aiohttp import ClientSession
import asyncio
import time
from fake_useragent import UserAgent


async def fetch_status(session: ClientSession, url: str) -> int:
    ua = UserAgent()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }
    async with session.get(url=url, headers=headers) as result:
        return result.status


async def main():
    async with ClientSession() as session:
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
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())
