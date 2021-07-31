import asyncio


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


async def job1():
    print(1)
    print(2)
    print(fib(36))
    print(3)


async def job2():
    print('job2-1')
    print('job2-2')
    print('job2-3')

async def job3():
    print('job3-1')
    print('job3-2')
    print('job3-3')


async def main():
    print('aaaa')
    asyncio.create_task(job2())
    asyncio.create_task(job1())
    asyncio.create_task(job3())
    print('bbbb')
    print('cccc')


asyncio.run(main())