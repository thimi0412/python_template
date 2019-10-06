from shimizu.test1 import hello
from src.main import plus


def test_1():
    assert 'hello' == hello()


def test_21():
    assert plus(1, 2) == 3
    assert plus(-2, -4) == -6
