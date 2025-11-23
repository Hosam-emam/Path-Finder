from src.mcp.server import mcp

if __name__ == "__main__":
    import asyncio
    asyncio.run(mcp.run(transport='sse'))