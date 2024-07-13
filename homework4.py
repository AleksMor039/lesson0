#2. Организуйте программу:
# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
# Вывести количество символов введённого текста
my_string=input("Как Ваше имя,", )
count=len(my_string)
print(count)

#3. Работа с методами строк:
print("моё имя", my_string.upper())
print("моё имя", my_string.lower())
#print("моё имя", my_string.replace(_old:'',_new:'') не могу понять как применить (.replace)
print("первая буква имени", my_string[0])
print("последняя буква имени", my_string[-1])
