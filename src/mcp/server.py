from mcp.server.fastmcp import FastMCP
from gitingest import ingest_async
import asyncio

mcp = FastMCP(
    name="GitIngest-MCP",
    instructions="This server is dedicated to ingesting remote github repos and generating an LLM-friendly version of your prompt",
    host="0.0.0.0",
    port=5000
    )

@mcp.tool()
async def async_ingest(source: str):
    """
    Asynchrounusly get the summary of the specified github repo
    and generate an LLM-firendly prompt version.
    
    ### Args:
        source (str): The github repository's url to be summarized
    
    ### Returns:
        The summary, tree, and the contents of the github repository
    """

    summary, tree, content = await ingest_async(source=source)

    return {
        "summary": summary,
        "tree": tree,
        "content": content
    }

if __name__ == "__main__":
    asyncio.run(mcp.run(transport='sse'))
