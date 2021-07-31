import asyncio
import httpx


async def req(delay):
    async with httpx.AsyncClient(timeout=20) as client:
        resp = await client.get(f'http://127.0.0.1:8000/sleep/{delay}')
        data = resp.json()
        print(data)


async def job1():
    print('进入job1里面')
    print(1)
    print(2)
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)
    await req(3)
    print('job1请求完成')
    print(4)
    print(5)
    print(6)


async def job2():
    print('进入 job2')
    print('一')
    print('二')
    print('三')
    await req(5)
    print('job2 请求完成')
    print('四')
    print('五')
    print('六')


async def task_without_await():
    print('瞬间执行1')
    print('瞬间执行2')
    print('瞬间执行3')


async def main():
    print('第1行')
    task1 = asyncio.create_task(job1())
    print('第2行')
    task5 = asyncio.create_task(task_without_await())
    task2 = asyncio.create_task(job2())
    # await task1
    print('第3行')
    print('第4行')
    print('第5行')
    await task2


asyncio.run(main())
