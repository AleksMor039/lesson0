def add_everything_up (a, b):
    try:
        sum = a + b
        return round(sum, 3)
    except TypeError as exc:
        return f'{a} и {b} это ошибка: {exc} просто склеим и пропустим'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))