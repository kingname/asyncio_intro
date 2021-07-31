import asyncio
import httpx


class Test:
    def __init__(self):
        self.name = 'kingname'

    async def req(self, url):
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            result = resp.json()
            print(result)


test = Test()
asyncio.run(test.req('http://xxx'))