# main.py
from fastmcp import FastMCP

# Create server
mcp = FastMCP(name="DemoServer2")  





# Register tools at module level
@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b






@mcp.tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together"""
    return a * b












#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid#Avid

# Run MCP server
if __name__ == "__main__":
    mcp.run()
