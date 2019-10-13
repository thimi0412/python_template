def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def times(a, b):
    return a * b


def div(a, b, is_floor=False):
    if is_floor:
        return a // b
    else:
        return a / b
