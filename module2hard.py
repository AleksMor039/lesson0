# Вариант  № 1
number = int(input('Введите число от 3 до 20:  '))

def search_of_key(number):
    key = ' '
    for i in range(1, number):
        for j in range(i+1, number+1):
            if number % (i + j) == 0:
                key += str(i) + str(j)
    return key
key = search_of_key(number)

print('Ключ к замку:', key)
print()
# Вариант № 2
import random
number = random.randrange(3, 21)
def search_of_key(number):
    key = ' '
    for i in range(1, number):
        for j in range(i+1, number+1):
            if number % (i + j) == 0:
                key += str(i) + str(j)
    return key
key = search_of_key(number)

print('Замок номер:', number, 'Ключ к замку:', key)

