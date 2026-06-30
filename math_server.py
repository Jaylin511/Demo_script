from fastmcp import FastMCP
import asyncio

mcp = FastMCP("server_name")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    print("Server starting on 127.0.0.1")
    mcp.run(transport="http", host="127.0.0.1", port=8000)