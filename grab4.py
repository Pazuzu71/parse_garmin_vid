import aiofiles
import os
from aiohttp import ClientSession
import asyncio
from fake_useragent import UserAgent
import time


async def fetch_status(session: ClientSession, url: str) -> tuple[int, str,  str]:
    ua = UserAgent()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }
    async with session.get(url=url, headers=headers) as result:
        file_name = url.split(r'/')[-1]
        # if result.status == 200:
        #     async with aiofiles.open(f'temp_async\\{file_name}', 'wb') as handle:
        #         await handle.write(result.content)
        return result.status, file_name, url


async def main():

    if not os.path.exists('temp'):
        os.mkdir('temp')
    if not os.path.exists('temp_async'):
        os.mkdir('temp_async')

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
        print(*status_codes, sep='\n')


# asyncio.get_event_loop().run_until_complete(main())
asyncio.run(main())
# try:
#     asyncio.run(main())
# except RuntimeError as e:
#     if 'Event loop is closed' in e:
#         print('Ошибка закрытия лупа')
