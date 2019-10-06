from shimizu.util.info import get_str_now


def test_2():
    date = get_str_now()
    assert isinstance(date, str)
