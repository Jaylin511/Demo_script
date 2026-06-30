""" import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8000/mcp")

async def call_tool(a: int, b: int):
    async with client:
        result = await client.call_tool("add", {"a": a, "b": b})
        print(result)

asyncio.run(call_tool(1,2))
"""


import asyncio
from fastmcp import Client

async def main():
    client = Client("http://127.0.0.1:8000/mcp")

    async with client:  # OPEN ONCE
        for i in range(5):
            result = await client.call_tool("add", {"a": i, "b": i})
            print(result)
            await asyncio.sleep(1)

    # connection closes here

asyncio.run(main())