import pytest

from test_library.node_config import NodeConfig


@pytest.fixture
def config():
    return NodeConfig()


def test_single_value_loading(config):
    config.load_from_lines(['block_log_info_print_file = ILOG'])
    assert config.block_log_info_print_file == 'ILOG'


def test_double_quoted_string_loading(config):
    config.load_from_lines([
        'account_history_rocksdb_path = "blockchain/account-history-rocksdb-storage"',
        'shared_file_dir = "blockchain"',
        'snapshot_root_dir = "snapshot"',
    ])

    # Output should not contain double quotes inside string
    assert config.account_history_rocksdb_path == 'blockchain/account-history-rocksdb-storage'
    assert config.shared_file_dir == 'blockchain'
    assert config.snapshot_root_dir == 'snapshot'
