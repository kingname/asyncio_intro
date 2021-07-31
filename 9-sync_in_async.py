import asyncio
import httpx
import time


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


async def do_request(sleep_time):
    async with httpx.AsyncClient(timeout=20) as session:
        resp = await session.get(f'http://127.0.0.1:8000/sleep/{sleep_time}')
        print(resp.json())


async def run_fib():
    result = fib(36)
    print(f'斐波拉契数列第36项是：{result}')

async def main():
    start = time.time()
    task1 = run_fib()
    task2 = do_request(5)
    await asyncio.gather(task1, task2)
    end = time.time()
    print(f'在协程中调用耗时的同步函数，耗时：{end - start}')


asyncio.run(main())