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
        url = 'https://connectvideo.garmin.com/msn-workout/Strength/S_147-A3.mp4'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} было равно {status}')


asyncio.run(main())
