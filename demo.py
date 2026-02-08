#!/usr/bin/env python3
"""
Demonstration of SICAP MCP Server

This script demonstrates the MCP server's capabilities by showing
the structure of tool calls and responses.
"""

import json


def demonstrate_tools():
    """Demonstrate the available tools and their usage"""
    
    print("=" * 70)
    print("SICAP MCP SERVER DEMONSTRATION")
    print("=" * 70)
    print()
    
    print("This MCP server provides 4 tools for interacting with the SICAP API:")
    print()
    
    tools = [
        {
            "name": "search_contracts",
            "description": "Search for public contracts in the SICAP database",
            "parameters": {
                "query": "construction (required)",
                "limit": "10 (optional, default: 10)",
                "offset": "0 (optional, default: 0)"
            },
            "example": 'search_contracts(query="infrastructure", limit=5)'
        },
        {
            "name": "get_contract_details",
            "description": "Get detailed information about a specific contract",
            "parameters": {
                "contract_id": "12345 (required)"
            },
            "example": 'get_contract_details(contract_id="ABC123")'
        },
        {
            "name": "get_organizations",
            "description": "Get information about organizations in the database",
            "parameters": {
                "name": "Ministry (optional)",
                "limit": "10 (optional, default: 10)",
                "offset": "0 (optional, default: 0)"
            },
            "example": 'get_organizations(name="Health", limit=5)'
        },
        {
            "name": "get_statistics",
            "description": "Get statistical information about contracts",
            "parameters": {
                "period": "monthly (optional)"
            },
            "example": 'get_statistics(period="yearly")'
        }
    ]
    
    for i, tool in enumerate(tools, 1):
        print(f"{i}. {tool['name']}")
        print(f"   Description: {tool['description']}")
        print(f"   Parameters:")
        for param, desc in tool['parameters'].items():
            print(f"      - {param}: {desc}")
        print(f"   Example: {tool['example']}")
        print()
    
    print("=" * 70)
    print("USAGE")
    print("=" * 70)
    print()
    print("To use this server:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run the server: python3 sicap_mcp_server.py")
    print("3. Configure your MCP client to connect to this server")
    print()
    print("Example MCP client configuration:")
    print()
    config = {
        "mcpServers": {
            "sicap": {
                "command": "python3",
                "args": ["./sicap_mcp_server.py"]
            }
        }
    }
    print(json.dumps(config, indent=2))
    print()
    
    print("=" * 70)
    print("ERROR HANDLING")
    print("=" * 70)
    print()
    print("All tools include robust error handling:")
    print("- Network errors are caught and returned as error messages")
    print("- HTTP errors include status codes")
    print("- Timeouts are set to 30 seconds")
    print("- Invalid responses are handled gracefully")
    print()
    
    print("=" * 70)
    print("API INFORMATION")
    print("=" * 70)
    print()
    print("Base URL: https://api.sicap.ai/v1/")
    print("OpenAPI Spec: https://api.sicap.ai/v1/openapi")
    print()
    print("Note: The API may require authentication or may be temporarily")
    print("unavailable. The server will handle these cases gracefully.")
    print()
    
    print("=" * 70)
    print("For more information, see:")
    print("- SICAP_MCP_README.md - Detailed API documentation")
    print("- SETUP_GUIDE.md - Setup and configuration guide")
    print("=" * 70)


if __name__ == "__main__":
    demonstrate_tools()
