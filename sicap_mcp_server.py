#!/usr/bin/env python3
"""
SICAP MCP Server

A Model Context Protocol (MCP) server that provides access to the SICAP API.
Uses fastmcp to expose SICAP API endpoints as MCP tools.
"""

import httpx
from typing import Optional, Dict, Any
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("SICAP API Server")

# SICAP API base URL
SICAP_API_BASE = "https://api.sicap.ai/v1"


def format_error_response(error: Exception) -> Dict[str, Any]:
    """
    Format an error into a consistent response structure.
    
    Args:
        error: The exception that occurred
    
    Returns:
        Dictionary with error information
    """
    if isinstance(error, httpx.HTTPError):
        return {
            "error": f"HTTP error occurred: {str(error)}",
            "status_code": getattr(error.response, 'status_code', None) if hasattr(error, 'response') else None
        }
    return {"error": f"An error occurred: {str(error)}"}


@mcp.tool()
async def search_contracts(
    query: str,
    limit: int = 10,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Search for public contracts in the SICAP database.
    
    Args:
        query: Search query string to find contracts
        limit: Maximum number of results to return (default: 10)
        offset: Offset for pagination (default: 0)
    
    Returns:
        Dictionary containing search results with contract information
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{SICAP_API_BASE}/contracts/search",
                params={
                    "q": query,
                    "limit": limit,
                    "offset": offset
                },
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return format_error_response(e)


@mcp.tool()
async def get_contract_details(
    contract_id: str
) -> Dict[str, Any]:
    """
    Get detailed information about a specific contract.
    
    Args:
        contract_id: The unique identifier of the contract
    
    Returns:
        Dictionary containing detailed contract information
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{SICAP_API_BASE}/contracts/{contract_id}",
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return format_error_response(e)


@mcp.tool()
async def get_organizations(
    name: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Get information about organizations in the SICAP database.
    
    Args:
        name: Optional organization name to filter by
        limit: Maximum number of results to return (default: 10)
        offset: Offset for pagination (default: 0)
    
    Returns:
        Dictionary containing organization information
    """
    async with httpx.AsyncClient() as client:
        try:
            params = {
                "limit": limit,
                "offset": offset
            }
            if name:
                params["name"] = name
            
            response = await client.get(
                f"{SICAP_API_BASE}/organizations",
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return format_error_response(e)


@mcp.tool()
async def get_statistics(
    period: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get statistical information about contracts in the SICAP database.
    
    Args:
        period: Optional time period for statistics (e.g., "monthly", "yearly")
    
    Returns:
        Dictionary containing statistical information
    """
    async with httpx.AsyncClient() as client:
        try:
            params = {}
            if period:
                params["period"] = period
            
            response = await client.get(
                f"{SICAP_API_BASE}/statistics",
                params=params if params else None,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return format_error_response(e)


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
