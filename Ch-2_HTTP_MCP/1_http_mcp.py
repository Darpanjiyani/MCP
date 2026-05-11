from fastmcp import FastMCP

# Create an instance of FastMCP
mcp = FastMCP()

@mcp.tool()
def fetch():
    '''Use this tool to Fetch data from a source.'''

    # Simulate fetching data from a source
    '''In a real application, this could be a database query, an API call, etc.'''
    return {"data": "Hello, World!"}

@mcp.tool()
def process():
    '''Use this tool to Process the fetched data.'''

    # Simulate processing the data
    '''In a real application, this could involve data transformation, analysis, etc.'''
    return {"processed_data": "Data has been processed!"}

if __name__ == "__main__":
    # Run the MCP server using HTTP transport
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8050)  