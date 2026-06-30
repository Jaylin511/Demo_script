from fastmcp import FastMCP
import asyncio

mcp = FastMCP("calculator")

@mcp.tool()
def add(a: float, b: float) -> float:
    """加法：返回 a + b"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """减法：返回 a - b"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """乘法：返回 a * b"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """除法：返回 a / b"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """幂运算：返回 base ** exponent"""
    return base ** exponent

@mcp.tool()
def sqrt(x: float) -> float:
    """平方根：返回 x 的算术平方根"""
    if x < 0:
        raise ValueError("不能对负数求平方根")
    return x ** 0.5

@mcp.tool()
def modulo(a: float, b: float) -> float:
    """取余：返回 a % b"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a % b

if __name__ == "__main__":
    print("Server starting on 127.0.0.1")
    mcp.run(transport="http", host="127.0.0.1", port=8000)