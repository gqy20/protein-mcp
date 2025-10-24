#!/bin/bash

# Protein MCP服务器启动脚本

echo "🧬 启动 Protein MCP Server"
echo "========================="

# 检查uv是否安装
if command -v uv &> /dev/null; then
    echo "✅ 使用uv启动服务器..."
    uv run python -m protein_mcp.server --transport http --port 37787
else
    echo "⚠️  uv未安装，使用Python直接启动..."
    python -m protein_mcp.server --transport http --port 37787
fi