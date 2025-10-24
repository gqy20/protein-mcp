"""测试配置和夹具"""

import os
import sys
import tempfile
from unittest.mock import Mock

import pytest

# 添加src到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from protein_mcp.utils import get_supported_formats


@pytest.fixture
def mock_http_response():
    """Mock HTTP响应的夹具"""

    def _mock_response(data, status_code=200):
        mock = Mock()
        mock.status = status_code
        mock.read.return_value = data.encode("utf-8") if isinstance(data, str) else data
        return mock

    return _mock_response


@pytest.fixture
def sample_graphql_response():
    """样本GraphQL响应数据"""
    return {
        "data": {
            "polymer_entities": [
                {
                    "rcsb_id": "1ABC",
                    "entity_polymer": {
                        "rcsb_entity_source_organism": {
                            "ncbi_taxonomy_id": 9606,
                            "scientific_name": "Homo sapiens",
                        },
                        "rcsb_polymer_entity": {
                            "pdbx_seq_one_letter_code": "ACDEFGHIKLMNPQRSTVWY",
                            "pdbx_seq_three_letter_code": "ALA CYS ASP GLU PHE GLY HIS ILE LYS LEU MET ASN PRO GLN ARG SER THR VAL TRP TYR",
                        },
                        "rcsb_polymer_entity_container_identifiers": {
                            "entity_id": "1",
                            "asym_ids": ["A"],
                            "auth_asym_ids": ["A"],
                        },
                    },
                }
            ]
        }
    }


@pytest.fixture
def sample_dssp_result():
    """样本DSSP计算结果"""
    return "HHHHEEEEECCCCCHHHHCCCC"


@pytest.fixture
def valid_pdb_ids():
    """有效的PDB ID列表"""
    return ["1abc", "2def", "3xyz", "4ABC", "1234"]


@pytest.fixture
def invalid_pdb_ids():
    """无效的PDB ID列表"""
    return ["abc", "123", "ABCDE", "12ab", "ab12", ""]


@pytest.fixture
def supported_formats():
    """支持的文件格式"""
    return get_supported_formats()


@pytest.fixture
def temp_output_dir():
    """临时输出目录"""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def mock_successful_download():
    """Mock成功的文件下载"""

    def _mock_download(url, path):
        # 创建一个模拟的PDB文件
        pdb_content = "HEADER    TEST PROTEIN              1ABC               12-JAN-24   1\n"
        with open(path, "w") as f:
            f.write(pdb_content)
        return True

    return _mock_download


@pytest.fixture
def server_instance():
    """FastMCP服务器实例"""
    from protein_mcp.server import create_server

    return create_server("test-server", "1.0.0-test")


# 测试工具函数
def assert_success_response(response):
    """断言成功响应"""
    assert response["success"] is True
    assert "data" in response
    assert "message" in response


def assert_error_response(response, error_type=None):
    """断言错误响应"""
    assert response["success"] is False
    assert "message" in response
    if error_type:
        assert error_type in response["message"]


def assert_response_contains_keys(response, keys):
    """断言响应包含指定键"""
    for key in keys:
        assert key in response["data"]
