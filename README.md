# Protein MCP Server

🧬 基于 FastMCP 的蛋白质数据访问服务器，提供3个核心工具用于蛋白质结构数据的搜索、获取和下载。

## 🎯 项目特色

✅ **从8个工具优化为3个核心工具** - 减少62.5%的复杂度
✅ **功能完全保持** - 所有原有功能完整保留
✅ **用户体验大幅提升** - 工具职责更清晰，学习成本更低
✅ **代码简洁高效** - 代码量减少39.2%，维护性显著提升

## 🚀 快速开始

### 使用uvx快速安装运行（推荐）

```bash
# 直接使用uvx运行MCP服务器
uvx protein-mcp --transport http --port 37787

# 查看帮助
uvx protein-mcp --help

# 启动STDIO模式
uvx protein-mcp --transport stdio
```

### 从PyPI安装

```bash
# 安装包
pip install protein-mcp

# 运行服务器
protein-mcp --transport http --port 37787

# 或使用uv运行
uv run protein-mcp --transport stdio
```

### 开发环境设置

```bash
# 克隆仓库
git clone <repository-url>
cd protein-mcp

# 安装开发依赖
uv sync --dev

# 启动服务器
uv run protein-mcp --transport http --port 37787
```

### 运行测试

```bash
# 快速测试
uv run pytest tests/quick_test.py -v

# 完整测试
uv run pytest tests/ -v --cov=src/protein_mcp
```

## 🛠️ 核心工具

### 1. find_protein_structures_tool
**蛋白质结构发现工具** - 搜索、示例、验证的统一入口

```python
# 获取热门示例
find_protein_structures()

# 搜索癌症靶点蛋白
find_protein_structures(category="癌症靶点")

# 验证PDB ID
find_protein_structures(pdb_id="1A3N")

# 关键词搜索
find_protein_structures(keywords="kinase", max_results=10)
```

### 2. get_protein_data_tool
**蛋白质综合数据工具** - 一次性获取所有蛋白质信息

```python
# 获取所有数据
get_protein_data("1A3N", ["all"])

# 获取基本信息和序列
get_protein_data("2HHB", ["basic", "sequence"])

# 获取特定链数据
get_protein_data("1A3N", ["all"], chain_id="A")
```

### 3. download_structure_tool
**结构文件工具** - 下载和管理蛋白质结构文件

```python
# 获取PDB文件内容
download_structure("1A3N", "pdb")

# 下载mmCIF格式并保存到本地
download_structure("2HHB", "mmcif", save_local=True)

# 获取快速MMTF格式
download_structure("6VSB", "mmtf")
```

## 🏗️ 项目结构

```
protein-mcp/
├── src/protein_mcp/           # 核心代码
│   ├── server.py             # FastMCP服务器
│   ├── tools.py              # 3个核心工具（已优化）
│   └── utils.py              # 工具函数
├── tests/                   # 测试文件
│   ├── quick_test.py         # 快速验证
│   ├── test_comprehensive.py # 综合测试
│   └── conftest.py          # 测试配置
├── .github/workflows/        # GitHub Actions
│   ├── code-quality.yml     # 代码质量检查
│   └── publish.yml         # 包发布流程
├── pyproject.toml           # 项目配置
└── README.md               # 项目文档
```

## 🔧 技术特性

### 数据源
- **RCSB Protein Data Bank** - 官方蛋白质数据库
- **混合API策略** - 结合REST API和PDB文件解析
- **自动降级** - API失败时自动使用文件解析

### 传输协议
- **HTTP传输** - 支持REST API调用
- **JSON-RPC 2.0** - 标准MCP协议
- **Server-Sent Events** - 实时响应格式

### 支持格式
- **PDB** - 标准蛋白质数据格式（推荐）
- **mmCIF** - 现代大分子晶体信息格式
- **MMTF** - 高性能二进制格式

## 📊 性能指标

- **快速查询**: < 1秒（示例、验证）
- **网络查询**: 2-6秒（搜索、数据获取）
- **文件下载**: 3-8秒（取决于文件大小）
- **成功率**: > 85%（网络相关功能）

## 🧪 测试体系

### 测试类型
- **快速测试**: 基本功能验证（< 10秒）
- **综合测试**: 全功能覆盖（~2分钟）
- **优化验证**: 代码优化效果确认

### 运行测试
```bash
# CI/CD集成
uv run pytest tests/quick_test.py -v

# 开发验证
uv run pytest tests/ -v --cov=src/protein_mcp

# 代码质量检查
uv run black --check src/ tests/
uv run ruff check src/ tests/
```

## 🌐 MCP集成

### Claude Desktop配置

```json
{
  "mcpServers": {
    "protein-mcp": {
      "command": "uvx protein-mcp",
      "args": ["--transport", "stdio"],
      "env": {}
    }
  }
}
```

### Claude Code 集成

#### 安装MCP服务器
```bash
# 使用Claude Code的slash命令安装
/mcp-server add protein-mcp

# 或者手动配置
# 创建 ~/.claude/mcp.json 文件
```

#### 配置文件格式 (`~/.claude/mcp.json`)
```json
{
  "mcpServers": {
    "protein-mcp": {
      "command": "uvx protein-mcp",
      "args": ["--transport", "stdio"],
      "env": {}
    }
  }
}
```

#### Claude Code中的使用方式
```bash
# 启动Claude Code时自动加载MCP服务器
# 在对话中直接使用蛋白质数据功能

# 示例对话：
# 用户: "帮我搜索血红蛋白相关的蛋白质结构"
# Claude: 自动调用 find_protein_structures_tool

# 用户: "获取蛋白质1A3N的完整信息"
# Claude: 自动调用 get_protein_data_tool
```

### CodeX集成

#### 安装和配置
```bash
# 安装MCP服务器
mcp install protein-mcp

# 查看已安装的MCP服务器
mcp list

# 启动CodeX时自动加载
codex --mcp protein-mcp
```

#### CodeX配置文件 (`~/.codex/mcp.json`)
```json
{
  "servers": {
    "protein-mcp": {
      "command": "uvx protein-mcp",
      "args": ["--transport", "stdio"],
      "workingDirectory": "~",
      "env": {
        "RCSB_CACHE_DIR": "~/.cache/rcsb",
        "PROTEIN_MCP_LOG_LEVEL": "info"
      }
    }
  }
}
```

### 通用MCP客户端集成

#### 方式1：使用uvx直接运行（推荐）
```python
import subprocess
import json

# 启动MCP服务器
server_process = subprocess.Popen([
    "uvx", "protein-mcp",
    "--transport", "stdio"
],
stdin=subprocess.PIPE,
stdout=subprocess.PIPE,
text=True)

# 发送初始化请求
init_request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {
            "name": "test-client",
            "version": "1.0.0"
        }
    }
}

server_process.stdin.write(json.dumps(init_request) + "\n")
server_process.stdin.flush()

# 发送工具调用请求
tool_request = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "find_protein_structures_tool",
        "arguments": {
            "keywords": "hemoglobin",
            "max_results": 5
        }
    }
}

server_process.stdin.write(json.dumps(tool_request) + "\n")
server_process.stdin.flush()

# 读取响应
response = server_process.stdout.readline()
result = json.loads(response)
```

#### 方式2：HTTP客户端集成
```python
import requests
import json

# 启动HTTP模式MCP服务器
import subprocess
import time
import threading

def start_http_server():
    subprocess.run([
        "uvx", "protein-mcp",
        "--transport", "http",
        "--port", "37787"
    ])

# 在后台线程启动服务器
server_thread = threading.Thread(target=start_http_server)
server_thread.daemon = True
server_thread.start()

# 等待服务器启动
time.sleep(2)

# HTTP API调用
mcp_base_url = "http://localhost:37787"

# 初始化连接
init_response = requests.post(f"{mcp_base_url}/mcp", json={
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {
            "tools": {}
        },
        "clientInfo": {
            "name": "python-client",
            "version": "1.0.0"
        }
    }
})

# 调用蛋白质搜索工具
search_response = requests.post(f"{mcp_base_url}/mcp", json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "find_protein_structures_tool",
        "arguments": {
            "keywords": "kinase inhibitor",
            "category": "drug target",
            "max_results": 10
        }
    }
})

# 调用蛋白质数据获取工具
data_response = requests.post(f"{mcp_base_url}/mcp", json={
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "get_protein_data_tool",
        "arguments": {
            "pdb_id": "1A3N",
            "data_types": ["basic", "sequence", "structure"]
        }
    }
})

# 调用结构文件下载工具
download_response = requests.post(f"{mcp_base_url}/mcp", json={
    "jsonrpc": "2.0",
    "id": 4,
    "method": "tools/call",
    "params": {
        "name": "download_structure_tool",
        "arguments": {
            "pdb_id": "6VSB",
            "file_format": "mmcif",
            "save_local": True
        }
    }
})
```

#### 方式3：编程方式导入
```python
# 直接导入和使用
from protein_mcp import create_server

# 创建服务器实例
server = create_server(
    name="custom-protein-mcp",
    version="0.1.0"
)

# 自定义启动方式
# STDIO模式（用于MCP协议）
server.run()

# 或HTTP模式（用于REST API）
import asyncio
async def start_http_mode():
    await server.run_http_async(host="localhost", port=37787)

asyncio.run(start_http_mode())
```

### 配置选项说明

#### 传输协议对比
| 协议 | 用途 | 优势 | 适用场景 |
|------|------|------|----------|
| **stdio** | 标准MCP协议 | 兼容性最好 | Claude Desktop/Code |
| **http** | REST API调用 | 易于调试 | Web应用集成 |
| **sse** | 实时推送 | 支持长连接 | 实时数据流 |

#### 环境变量配置
```json
{
  "mcpServers": {
    "protein-mcp": {
      "command": "uvx protein-mcp",
      "args": ["--transport", "stdio"],
      "env": {
        "PROTEIN_MCP_LOG_LEVEL": "debug",
        "RCSB_API_TIMEOUT": "30",
        "PROTEIN_MCP_CACHE_DIR": "/tmp/protein_cache",
        "PROTEIN_MCP_MAX_RETRIES": "3"
      }
    }
  }
}
```

## 📈 优化成果

| 指标 | 优化前 | 优化后 | 改进 |
|------|--------|--------|------|
| 工具数量 | 8个 | 3个 | ⬇️ 62.5% |
| 代码行数 | 1025行 | 623行 | ⬇️ 39.2% |
| 函数数量 | 16个 | 7个 | ⬇️ 56.3% |
| 用户复杂度 | 高（需了解8个工具） | 低（只需3个核心工具） | ⬇️ 显著改善 |

## 📝 开发配置

- **Python**: >= 3.10
- **依赖管理**: uv
- **FastMCP**: >= 2.12.0
- **代码质量**: 自动化格式化和检查（Black + Ruff + MyPy）
- **测试覆盖**: 核心功能100%覆盖
- **CI/CD**: GitHub Actions自动化流程

## 📦 包信息

- **包名**: `protein-mcp`
- **版本**: 0.1.0
- **PyPI**: https://pypi.org/project/protein-mcp/
- **安装命令**: `pip install protein-mcp` 或 `uvx protein-mcp`

## 🔧 开发环境

### 本地开发
```bash
# 安装开发依赖
uv sync --dev

# 运行服务器
uv run protein-mcp --transport http --port 8080

# 运行测试
uv run pytest tests/ -v

# 代码格式化
uv run black src/ tests/
uv run ruff check src/ tests/ --fix
uv run isort src/ tests/
```

### 预提交检查
```bash
# 安装pre-commit hooks
pip install pre-commit
pre-commit install

# 手动运行检查
pre-commit run --all-files
```

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🤝 贡献

欢迎提交Issue和Pull Request！

### 开发流程
1. Fork项目
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建Pull Request

---

**🧬 Protein MCP Server - 让蛋白质数据访问变得简单而高效！**