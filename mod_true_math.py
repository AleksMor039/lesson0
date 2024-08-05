from math import inf


def divide(first, second):

    try:
        x = first / second
    except (ZeroDivisionError, ValueError):
        return inf
    else:
        return int(x)

