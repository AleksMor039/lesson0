def divide(first, second):
    try:
        i = first / second
    except (ZeroDivisionError, ValueError):
        return str('Ошибка')
    else:
        return int(i)
