def divide(first, second):
    try:
        i = first / second
    except ZeroDivisionError:
        return str('Ошибка')
    else:
        return i
