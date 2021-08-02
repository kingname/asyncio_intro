import asyncio
import httpx
import time

@property
async def req(delay, sem):
    print(f'请求一个延迟为{delay}秒的接口')
    async with sem:
        async with httpx.AsyncClient(timeout=20) as client:
            resp = await client.get(f'http://127.0.0.1:8000/sleep/{delay}')
            result = resp.json()
            print(result)
    await asyncio.sleep(60)


async def main():
    start = time.time()
    delay_list = [3, 6, 1, 8, 2, 4, 5, 2, 7, 3, 9, 8]
    task_list = []
    sem = asyncio.Semaphore(3)
    for delay in delay_list:
        task = asyncio.create_task(req(delay, sem))
        task_list.append(task)
    await asyncio.gather(*task_list)

    end = time.time()
    print(f'一共耗时：{end - start}')

asyncio.run(main())
