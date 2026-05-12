from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os


# {
#     "mcpServers": {
#         "ddg-search": {
#             "command": "uvx",
#             "args": ["duckduckgo-mcp-server"]
#         }
#     }
# }

async def main():

    # create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(

        # MCP Server COnfiguration (JSON)
        {
            "ddg-search":{
                "transport": "stdio",
                "command": "uvx",
                "args": ["duckduckgo-mcp-server"]
            }
        }
 )

    # List the tools
    tools = await client.get_tools()
    for tool in tools:
        print("Available tool:", tool.name)

    # result = await client.invoke("ddg-search", "search", {"query": "What is the capital of France?"})
    # print("Search result:", result)

    fetch_tool = tools[0]
    result = await fetch_tool.ainvoke({"query": "What is the capital of France?"})
    print("Search result:", result)

if __name__ == "__main__":
    asyncio.run(main())