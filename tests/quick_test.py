#!/usr/bin/env python3
"""
Protein MCP服务器快速测试
用于日常验证服务器基本功能
"""

import json
import os
import sys

import requests

# 禁用代理
os.environ.pop("http_proxy", None)
os.environ.pop("https_proxy", None)


def quick_test():
    """快速测试基本功能"""
    base_url = "http://localhost:37787/mcp"
    headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}

    print("⚡ Protein MCP服务器快速测试")
    print("=" * 40)

    # 1. 初始化
    print("\n1️⃣ 初始化会话...")
    init_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "quick-test", "version": "1.0.0"},
        },
    }

    try:
        response = requests.post(
            base_url, json=init_payload, headers=headers, timeout=10, proxies={}
        )
        if response.status_code == 200:
            session_id = response.headers.get("Mcp-Session-Id")
            print(f"✅ 会话ID: {session_id}")
        else:
            print(f"❌ 初始化失败: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 初始化错误: {str(e)}")
        return False

    # 2. 发送initialized通知
    try:
        notif_headers = headers.copy()
        if session_id:
            notif_headers["Mcp-Session-Id"] = session_id

        notif_payload = {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}

        requests.post(base_url, json=notif_payload, headers=notif_headers, timeout=10, proxies={})
        print("✅ initialized通知已发送")
    except Exception as e:
        print(f"❌ 通知发送失败: {str(e)}")

    def parse_sse_response(response_text):
        """解析SSE响应"""
        if "event: message" in response_text:
            lines = response_text.split("\n")
            for line in lines:
                if line.startswith("data: "):
                    try:
                        return json.loads(line[6:])
                    except json.JSONDecodeError:
                        continue
        return None

    # 3. 测试工具列表
    print("\n2️⃣ 检查工具列表...")
    tools_headers = headers.copy()
    if session_id:
        tools_headers["Mcp-Session-Id"] = session_id

    tools_payload = {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}

    try:
        response = requests.post(
            base_url, json=tools_payload, headers=tools_headers, timeout=10, proxies={}
        )
        if response.status_code == 200:
            data = parse_sse_response(response.text)
            if data:
                tools = data.get("result", {}).get("tools", [])
                print(f"✅ 工具数量: {len(tools)}")
                tool_names = [tool.get("name") for tool in tools]
                for name in tool_names:
                    print(f"   • {name}")
            else:
                print("❌ 无法解析工具列表")
                return False
        else:
            print(f"❌ 获取工具列表失败: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 工具列表错误: {str(e)}")
        return False

    # 4. 测试默认示例功能
    print("\n3️⃣ 测试默认示例功能...")
    test_headers = headers.copy()
    if session_id:
        test_headers["Mcp-Session-Id"] = session_id

    test_payload = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {"name": "find_protein_structures_tool", "arguments": {}},
    }

    try:
        response = requests.post(
            base_url, json=test_payload, headers=test_headers, timeout=30, proxies={}
        )
        if response.status_code == 200:
            data = parse_sse_response(response.text)
            if data:
                result = data.get("result", {})
                structured_content = result.get("structuredContent", {})
                success = structured_content.get("success", False)
                message = structured_content.get("message", "")

                print(f"✅ 测试结果: {success}")
                print(f"   响应: {message}")
            else:
                print("❌ 无法解析测试响应")
                return False
        else:
            print(f"❌ 测试请求失败: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 测试错误: {str(e)}")
        return False

    print("\n🎉 快速测试完成！服务器运行正常。")
    return True


if __name__ == "__main__":
    success = quick_test()
    sys.exit(0 if success else 1)
