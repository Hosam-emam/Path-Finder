import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

SERVER_URL = "http://localhost:5000/sse"

async def run_gitingest_client():
    """Run the MCP Gitingest Client"""

    async with sse_client(SERVER_URL) as (read, write):
        async with ClientSession(read, write) as session:
            
            await session.initialize()
            print("Session Initialized Successfully.")

            tools = await session.list_tools()

            print(f"Available tools:")
            for tool in tools:
                print(f"- {tool}")


if __name__ == "__main__":
    asyncio.run(run_gitingest_client())
