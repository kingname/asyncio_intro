import asyncio
import httpx
import time


async def do_request(sleep_time):
    async with httpx.AsyncClient(timeout=20) as session:
        resp = await session.get(f'http://127.0.0.1:8000/sleep/{sleep_time}')
        print(resp.json())


async def main():
    start = time.time()
    task1 = asyncio.create_task(do_request(3))
    task2 = asyncio.create_task(do_request(5))
    task3 = asyncio.create_task(do_request(8))
    await task3  # 用耗时最长的任务防止退出函数
    await task1
    await task2
    # for i in range(10):
    #     await asyncio.sleep(1)  # 如果不知道谁耗时长，也可以用asyncio.sleep
    end = time.time()
    print(f'使用协程请求三个网址，耗时：{end - start}')


asyncio.run(main())