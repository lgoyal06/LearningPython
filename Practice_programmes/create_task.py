import asyncio
import time

async def co_task(msg):
    await asyncio.sleep(2)
    print(msg)

async def main():
    task1 = asyncio.create_task(co_task("Hello"))
    task2 = asyncio.create_task(co_task(" World !!"))
    
    await task1
    await task2

asyncio.run(main())
