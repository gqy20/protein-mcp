# Protein MCP 测试指南

## 测试文件说明

### 测试脚本
- **quick_test.py**: 快速验证服务器基本功能 (< 10秒)
- **test_comprehensive.py**: 全面测试所有工具功能
- **test_cleaned_tools.py**: 验证代码优化效果

### 使用方法

#### 1. 快速测试
```bash
# 直接运行
python tests/quick_test.py

# 或使用脚本
./scripts/quick_test.sh
```

#### 2. 完整测试
```bash
# 运行交互式测试脚本
./scripts/run_tests.sh

# 或直接运行综合测试
python tests/test_comprehensive.py
```

#### 3. 单独测试各个功能
```bash
# 快速验证基本功能
python tests/quick_test.py

# 验证优化后的工具
python tests/test_cleaned_tools.py

# 运行完整功能测试
python tests/test_comprehensive.py
```

## 测试环境要求

1. **服务器运行**: 确保MCP服务器在 `http://localhost:37787` 运行
2. **网络连接**: 需要访问RCSB API
3. **Python依赖**: requests, json, os, sys, time

## 测试结果解读

### 成功标准
- **快速测试**: 100% 通过
- **综合测试**: ≥ 80% 通过率
- **响应时间**: < 30秒

### 常见问题

1. **连接超时**
   - 检查服务器是否运行: `curl http://localhost:37787/mcp`
   - 重新启动服务器: `./scripts/start_server.sh`

2. **代理问题**
   - 测试脚本会自动禁用代理
   - 手动禁用: `unset http_proxy https_proxy`

3. **端口占用**
   - 查找占用进程: `lsof -i :37787`
   - 终止进程: `kill -9 <PID>`

## CI/CD 集成

在CI/CD流水线中使用快速测试：

```bash
# 设置环境
unset http_proxy https_proxy

# 运行测试
./scripts/quick_test.sh
```

GitHub Actions示例：
```yaml
- name: Test Protein MCP Server
  run: |
    ./scripts/quick_test.sh
```