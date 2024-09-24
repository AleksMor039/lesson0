# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))  # приним.2парам/ возврат х=у/ идёт по first и second
print(result)


# Замыкание:
def get_advanced_writer(file_name): #ф-ия высшего порядка
    def write_everything(*data_set): #ф-ия внутри функции
        with open(file_name, mode='w', encoding='UTF-8') as file:
            for i in data_set:
                file.write(str(i))
                file.write('\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice


class MysticBall:
    def __init__(self, *words): # исп*args для передачи неопределён.числа неимен.аргум.
        self.words = words

    def __call__(self):
        words = choice(self.words)
        return words


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Как так то?')
print(first_ball())
print(first_ball())
print(first_ball())
