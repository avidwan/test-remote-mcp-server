from fastmcp import FastMCP

# Register tools at module level
@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b

@mcp.tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together"""
    return a * b


# Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    # mcp.run()