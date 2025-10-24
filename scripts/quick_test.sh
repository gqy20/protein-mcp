#!/bin/bash

# 快速测试脚本 - 用于CI/CD集成

echo "⚡ Protein MCP 快速测试"
echo "===================="

# 禁用代理以避免本地连接问题
unset http_proxy https_proxy

# 运行快速测试
python tests/quick_test.py

# 返回测试结果
if [ $? -eq 0 ]; then
    echo "✅ 快速测试通过"
    exit 0
else
    echo "❌ 快速测试失败"
    exit 1
fi