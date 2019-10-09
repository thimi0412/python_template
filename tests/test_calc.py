from mycalc.calc import add
import pytest


@pytest.mark.parametrize('a,b,ans', [
    (1, 1, 2),
    (3, 5, 8),
    (-1, 6, 5),
])
def test_add(a, b, ans):
    assert add(a, b) == ans
