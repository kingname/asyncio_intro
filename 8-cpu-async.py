import asyncio
import httpx
import time


async def fib(n):
    if n in [1, 2]:
        return 1
    return await fib(n - 1) + await fib(n - 2)


async def do_request(sleep_time):
    async with httpx.AsyncClient(timeout=20) as session:
        resp = await session.get(f'http://127.0.0.1:8000/sleep/{sleep_time}')
        print(resp.json())

async def main():
    start = time.time()
    task1 = fib(36)
    task2 = do_request(5)
    await asyncio.gather(task1, task2)
    end = time.time()
    print(f'强行把 CPU 密集型代码放到 async 中，耗时：{end - start}')


asyncio.run(main())