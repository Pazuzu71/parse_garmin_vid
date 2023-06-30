import requests
from fake_useragent import UserAgent
from time import sleep
from random import randint
import os


def is_accessible(file_name):
    ua = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }
    url = f'https://connectvideo.garmin.com/msn-workout/Strength/{file_name}'
    r = requests.get(url=url, headers=headers)
    print(f'ищем {file_name}')
    if r.status_code == 200:
        return True
    else:
        print(f'https://connectvideo.garmin.com/msn-workout/Strength/{file_name}')
        print(r.status_code)
        print(f'не найден {file_name}')
        return False


def download(file_name):
    ua = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }
    url = f'https://connectvideo.garmin.com/msn-workout/Strength/{file_name}'
    r = requests.get(url=url, headers=headers)

    with open(f'temp\\{file_name}', 'wb') as f:
        f.write(r.content)
    print(f'{file_name} скачан')


def main():

    if not os.path.exists('temp'):
        os.mkdir('temp')
    for k in range(1, 3):
        for i in range(1000):
            for j in "ABCDE":
                if i < 10:
                    num = f'00{i}'
                elif i < 100:
                    num = f'0{i}'
                else:
                    num = str(i)
                file_name = f'S_{num}-{j}{k}.mp4'
                sleep(randint(1, 5))
                if is_accessible(file_name):
                    download(file_name)
                else:
                    break


if __name__ == '__main__':
    main()
