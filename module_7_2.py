# комментарии для себя

file_name = 'test_mod_7_2.txt'

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    strings_position = {}
    file = open(file_name, 'w', encoding='utf-8')
    for line_number, string in enumerate(strings, start=1):  # enumerate (iterable, start) ф-ия принимает набор данных
        # в качестве параметра и возвращает объект enumerate
        # - в формате пар ключ-значение
        # ключ - индекс элемента, значение - сами элементы)
        start_byte = file.tell()  # получить номер байта начала строки
        file.write(string + '\n')  # \'n' - спец.символ перехода на след.строку
        strings_position[(line_number, start_byte)] = string  # (ключ номер строки, байт начала строки)
        # значение - строка
    file.close()
    return strings_position


result = custom_write('test_mod_7_2.txt', info)
for elem in result.items():
    print(elem)
