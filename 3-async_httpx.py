import asyncio
import httpx


async def request():
    async with httpx.AsyncClient() as client:
        response = await client.get('http://127.0.0.1:8000/sleep/3')
        result = response.json()
        print(result)


asyncio.run(request())