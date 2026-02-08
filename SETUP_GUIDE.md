# SICAP MCP Server Setup Guide

## Quick Start

This guide will help you set up and use the SICAP MCP server.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `fastmcp` - The FastMCP framework for building MCP servers
- `httpx` - HTTP client for making async API requests
- `pydantic` - Data validation library

### 2. Verify Installation

Run the test script to verify everything is working:

```bash
python3 test_sicap_mcp.py
```

You should see:
```
✓ MCP Server tests passed!
```

## Running the Server

### Standalone Mode

To run the server in standalone mode:

```bash
python3 sicap_mcp_server.py
```

The server will start and listen for MCP protocol messages on stdin/stdout.

### Integration with MCP Clients

#### Claude Desktop Configuration

1. Open your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. Add the SICAP server configuration:

```json
{
  "mcpServers": {
    "sicap": {
      "command": "python3",
      "args": [
        "/absolute/path/to/sicap_mcp_server.py"
      ]
    }
  }
}
```

3. Replace `/absolute/path/to/` with the actual path to the server file.

4. Restart Claude Desktop.

#### Other MCP Clients

For other MCP-compatible clients, use the example configuration in `mcp_config_example.json` as a starting point.

## Available Tools

Once the server is running, the following tools are available:

### 1. search_contracts

Search for public contracts in the SICAP database.

```
search_contracts(
    query="construction",
    limit=10,
    offset=0
)
```

### 2. get_contract_details

Get detailed information about a specific contract.

```
get_contract_details(contract_id="12345")
```

### 3. get_organizations

Get information about organizations.

```
get_organizations(
    name="Ministry",
    limit=10,
    offset=0
)
```

### 4. get_statistics

Get statistical information about contracts.

```
get_statistics(period="monthly")
```

## API Notes

- The server connects to `https://api.sicap.ai/v1/`
- The API may require authentication or may be temporarily unavailable
- All tools include error handling and will return descriptive error messages if the API is unreachable

## Troubleshooting

### Import Errors

If you see import errors, make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### API Connection Issues

If the API is not accessible:
- Check your internet connection
- Verify the API endpoint is available
- The API may require authentication (check SICAP documentation)
- Use the test script to diagnose: `python3 test_sicap_mcp.py`

### Server Not Responding

1. Check that Python 3.8+ is installed: `python3 --version`
2. Verify the server file path in your MCP client configuration
3. Check the MCP client logs for error messages

## Development

### Testing Changes

After modifying the server, run the test suite:

```bash
python3 test_sicap_mcp.py
```

### Adding New Tools

To add new SICAP API endpoints:

1. Add a new function decorated with `@mcp.tool()`
2. Follow the async function pattern used by existing tools
3. Include proper error handling
4. Update the documentation

Example:

```python
@mcp.tool()
async def get_new_endpoint(param: str) -> Dict[str, Any]:
    """
    Description of what this tool does.
    
    Args:
        param: Description of parameter
    
    Returns:
        Dictionary with results
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{SICAP_API_BASE}/new-endpoint/{param}",
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Error: {str(e)}"}
```

## Support

For issues with:
- **This MCP server**: Check the GitHub repository
- **FastMCP framework**: Visit https://github.com/jlowin/fastmcp
- **SICAP API**: Check SICAP documentation at https://api.sicap.ai/

## License

MIT License
