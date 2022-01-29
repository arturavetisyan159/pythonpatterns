import asyncio
import aiohttp
import time
import requests

URL = "http://loremflickr.com/1920/1080"


def write_image(data, name):
    with open(f"images/{name}.jpg", "wb") as f:
        f.write(data)

def fetch_sync(tid: int):
    print(f"Задача №{tid} началась!")
    start_time = time.time()
    response = requests.get(URL).content
    write_image(response, tid)
    print(f"Задача №{tid} закончилась!")

async def fetch_async(tid: int):
    print(f"Задача №{tid} началась!")
    start_time = time.time()
    async aiohttp.ClientSession() as session:
        async with session.get(URL) as response:

    print(f"Задача №{tid} закончилась!")



