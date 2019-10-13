from mycalc.calc import (
    add,
    sub
)
import pytest


@pytest.mark.parametrize('a,b,ans', [
    (1, 1, 2),
    (3, 5, 8),
    (-1, 6, 5),
])
def test_add(a, b, ans):
    assert add(a, b) == ans


@pytest.mark.parametrize('a,b,ans', [
    (4, 2, 2),
    (1, 4, -3),
    (-1, -4, 3)
])
def test_sub(a, b, ans):
    assert sub(a, b) == ans
