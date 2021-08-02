import asyncio
import httpx
import time


async def do_request(sleep_time):
    async with httpx.AsyncClient(timeout=20) as session:
        resp = await session.get(f'http://127.0.0.1:8000/sleep/{sleep_time}')
        print(resp.json())


async def main():
    start = time.time()
    task1 = do_request(3)
    task2 = do_request(5)
    task3 = do_request(8)
    task_list = [task1, task2, task3]
    await asyncio.gather(*task_list)
    end = time.time()
    print(f'使用协程请求三个网址，耗时：{end - start}')


asyncio.run(main())