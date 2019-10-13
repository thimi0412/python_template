from mycalc.calc import (
    add,
    sub,
    times,
    div
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


@pytest.mark.parametrize('a,b,ans', [
    (2, 3, 6),
    (-3, 4, -12),
    (-5, -6, 30)
])
def test_times(a, b, ans):
    assert times(a, b) == ans


@pytest.mark.parametrize('a,b,is_floor,ans', [
    (8, 4, False, 2),
    (5, 2, False, 2.5),
    (9, 4, True, 2),
    (1, 2, True, 0)
])
def test_div(a, b, is_floor, ans):
    assert div(a, b, is_floor=is_floor) == ans
