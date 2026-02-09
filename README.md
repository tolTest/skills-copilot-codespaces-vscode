# SICAP MCP Server

A Model Context Protocol (MCP) server that provides access to the SICAP public API (https://api.sicap.ai/v1/openapi).

## Overview

This MCP server uses [fastmcp](https://github.com/jlowin/fastmcp) to expose SICAP API endpoints as MCP tools, allowing AI assistants to interact with public contract data.

## Features

The server provides the following tools:

- **search_contracts**: Search for public contracts in the SICAP database
- **get_contract_details**: Get detailed information about a specific contract
- **get_organizations**: Get information about organizations
- **get_statistics**: Get statistical information about contracts

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

To start the MCP server:

```bash
python sicap_mcp_server.py
```

### Using with MCP Clients

The server can be used with any MCP-compatible client. Configure your client to connect to this server using the stdio transport.

Example configuration for Claude Desktop or other MCP clients:

```json
{
  "mcpServers": {
    "sicap": {
      "command": "python",
      "args": ["/path/to/sicap_mcp_server.py"]
    }
  }
}
```

## Tools Documentation

### search_contracts

Search for public contracts in the SICAP database.

**Parameters:**
- `query` (string, required): Search query string to find contracts
- `limit` (integer, optional): Maximum number of results to return (default: 10)
- `offset` (integer, optional): Offset for pagination (default: 0)

**Example:**
```python
search_contracts(query="construction", limit=5)
```

### get_contract_details

Get detailed information about a specific contract.

**Parameters:**
- `contract_id` (string, required): The unique identifier of the contract

**Example:**
```python
get_contract_details(contract_id="12345")
```

### get_organizations

Get information about organizations in the SICAP database.

**Parameters:**
- `name` (string, optional): Organization name to filter by
- `limit` (integer, optional): Maximum number of results to return (default: 10)
- `offset` (integer, optional): Offset for pagination (default: 0)

**Example:**
```python
get_organizations(name="Ministry", limit=10)
```

### get_statistics

Get statistical information about contracts in the SICAP database.

**Parameters:**
- `period` (string, optional): Time period for statistics (e.g., "monthly", "yearly")

**Example:**
```python
get_statistics(period="monthly")
```

## API Information

This server interfaces with the SICAP API at `https://api.sicap.ai/v1/`. The API provides access to public procurement contract information.

## Requirements

- Python 3.8+
- fastmcp
- httpx
- pydantic

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
