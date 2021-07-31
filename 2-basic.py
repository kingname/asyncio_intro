import asyncio


async def i_am_async_func():
    print('我是一个异步函数')
    return 'kingname'


async def i_will_call_you():
    print('我来调用异步函数')
    result = await i_am_async_func()
    print('异步函数返回的值是：', result)


async def matryoshka():
    print('我去调用那个调用异步函数的异步函数')
    await i_will_call_you()


asyncio.run(matryoshka())