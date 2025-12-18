from tools.safety_guard import is_safe


def test_safety_guard():
    assert is_safe("print('hello')")
    assert not is_safe("rm -rf /")
