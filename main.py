from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("openshift-backplane")

#@mcp.tool()
#async def login_cluster(cluster_id: str) -> str:
#    ""Log into an end cluster.

#    Args:
#        cluster_id: 

@mcp.tool()
async def cluster_info(cluster_id: str) -> str:
    """Get information about cluster.
    
    Args:
        cluster_id: a string 32 or 36 characters long identifying a cluster."""
    
    info = "Cluster type: ROSA HCP"
    return info

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')