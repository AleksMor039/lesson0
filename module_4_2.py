# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции inner_function,
# функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# # Попробуйте вызывать inner_function вне функции test_function
# и посмотрите на результат выполнения программы

def test_function():
    print('Я объемлющее для inner_function') # пояснение для преподавателя: немного отошёл от задания, пытался понять что есть объемлющее, а что локальное
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function() # вызов данной функции вне функции test_function приводит к ошибке, если я правильно понял лекцию это связано с тем что локальное
                     # нельзя достать из объемлющего. Если понял неправильно прошу разъяснить.


test_function()
