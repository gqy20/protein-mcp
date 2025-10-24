#!/bin/bash

# Protein MCP服务器测试脚本

echo "🧪 运行 Protein MCP 服务器测试"
echo "============================"

# 检查服务器是否运行
echo "1️⃣ 检查服务器状态..."
if curl -s http://localhost:37787/mcp > /dev/null 2>&1; then
    echo "✅ 服务器正在运行"
else
    echo "❌ 服务器未运行，请先启动服务器："
    echo "   ./scripts/start_server.sh"
    exit 1
fi

# 运行快速测试
echo ""
echo "2️⃣ 运行快速测试..."
python tests/quick_test.py
if [ $? -eq 0 ]; then
    echo "✅ 快速测试通过"
else
    echo "❌ 快速测试失败"
    exit 1
fi

# 询问是否运行综合测试
echo ""
echo "3️⃣ 是否运行综合测试？(y/n)"
read -r response
if [[ "$response" =~ ^[Yy]$ ]]; then
    echo "运行综合测试..."
    python tests/test_comprehensive.py
    if [ $? -eq 0 ]; then
        echo "✅ 综合测试通过"
    else
        echo "❌ 综合测试失败"
        exit 1
    fi
else
    echo "跳过综合测试"
fi

echo ""
echo "🎉 所有测试完成！"