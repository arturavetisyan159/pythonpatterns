import time
import asyncio

import requests
import aiohttp



# цикл сбытий - управляет выполнением различных задач
# корутина - специальная функция, которая не блокитрует контекст исполнения в событийном цикле
# футура (фьючерс / промис) - объекты, в которых хранятся результаты вычислений корутин


# def sync_do_smth(tid: int):
#     print(f"Задача {tid} запущена")
#     time.sleep(2)
#     print(f"Задача {tid} выполнена")
#
# async def async_do_smth(tid: int):
#     print(f"Задача {tid} запущена")
#     await asyncio.sleep(2)
#     # print(1 + 1)
#     print(f"Задача {tid} выполнена")
#
#
# def main():
#     start_time = time.time()
#     sync_do_smth(1)
#     sync_do_smth(2)
#     print(f"Время исполнения программы: {time.time() - start_time} сек")

# async def async_main():
    # await asyncio.gather(async_do_smth(1), async_do_smth(2))

URL = 'https://ya.ru'
MAX_REQUESTS = 3


def fetch_sync(tid: int):
    print(f"Синхронная задача номер {tid} началась!")
    response = requests.get(URL)
    date = response.headers['Date']
    print(f"Синхронная задача номер {tid} выполнена! -> {date}")

async def fetch_async(tid: int):
    print(f"Асинхронная задача номер {tid} началась!")
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            date = response.headers['Date']
    print(f"Асинхронная задача номер {tid} выполнена! -> {date}")

def synchronious():
    start_time = time.time()
    for i in range(1, MAX_REQUESTS + 1):
        fetch_sync(i)
    print(f"Время исполнения синхронной программы: {time.time() - start_time} сек")

async def asynchronious():
    start_time = time.time()
    tasks = []
    for i in range(1, MAX_REQUESTS + 1):
        tasks.append(fetch_async(i))
    await asyncio.gather(*tasks)
    print(f"Время исполнения асинхронной программы: {time.time() - start_time} сек")


if __name__ == "__main__":
    start_time = time.time()
    # asyncio.run(async_main())
    # loop = asyncio.get_event_loop() # создаем событийный цикл
    # tasks = [loop.create_task(async_do_smth(1)), loop.create_task(async_do_smth(2)), loop.create_task(async_do_smth(3))]
    # wait_tasks = asyncio.wait(tasks)
    # loop.run_until_complete(wait_tasks)
    # loop.close()

    synchronious()
    asyncio.run(asynchronious())
    print(f"Время исполнения всей программы: {time.time() - start_time} сек")


