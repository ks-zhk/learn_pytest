import pytest

def f():
    raise SystemExit(0)
def test_mytest():
    with pytest.raises(SystemExit):
        f()