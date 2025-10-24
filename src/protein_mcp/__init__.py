"""Protein MCP - 基于FastMCP的蛋白质数据访问工具"""

__version__ = "1.0.0"
__author__ = "Protein MCP Team"
__email__ = "team@protein-mcp.org"

from .server import create_server, main
from .tools import register_all_tools

__all__ = ["create_server", "main", "register_all_tools"]
