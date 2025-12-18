from utils.json_utils import save_json, load_json
import os


def test_memory_save_load(tmp_path):
    path = tmp_path / "test.json"
    data = {"a": 1}
    save_json(path, data)
    loaded = load_json(path)
    assert loaded["a"] == 1
