from typing import Any
from mcp.server.fastmcp import FastMCP
import subprocess

async def run_command(args: list) -> str:
    """Runs the command from provided arguments.

    Args:
        args: args

    Returns:
        A tuple containing (stdout_string, stderr_string)."""

    try:
        process = subprocess.run(args, capture_output=True, text=True, check=False)
        stdout_string = process.stdout
        stderr_string = process.stderr
        return stdout_string, stderr_string
    except FileNotFoundError:
        return "", f"Error: command wasn't found, you're missing the onboarding step to install '{args[0]}'."

# Initialize FastMCP server
mcp = FastMCP("openshift-backplane")

@mcp.tool()
async def cluster_login(cluster_id: str) -> str:
    """Log into a cluster to be able to issues kubectl commands.
    Use once per session unless connection is broken or user explicitly states they want to connect to a different cluster.

    Args:
        cluster_id: a string 32 or 36 characters long identifying a cluster."""

    #(stdout, stderr) = await run_command(["ocm", "whoami"])
    return "You are logged in"

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