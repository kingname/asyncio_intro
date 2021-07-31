import asyncio
import httpx
import time


async def request(num):
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(f'http://127.0.0.1:8000/sleep/{num}')
        result = response.json()
        print(result)


async def main():
    start = time.time()
    await request(3)
    await request(5)
    await request(8)
    end = time.time()
    print(f'使用协程请求三个网址，耗时：{end - start}')


asyncio.run(main())