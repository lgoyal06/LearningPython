import sys
import asyncio

async def question():
  #Complete this coroutine
  print("Is asyncio better for IO bound programs than the CPU bound ones?")
  await answer()
  print("Is async a keyword in the latest Python3?")
  await answer()
  print("Is event loop the heart of an asyncio program?")
  await answer()



async def answer():
  #Complete this coroutine
  print("Yes, it is!")
  #await asyncio.sleep(1)

asyncio.run(question())
