tuple=([1,2,3], True, 'hello')
immutable_var=tuple
print(immutable_var)
# tuple[1]=False # если раскомментировать, то будет ошибка
# TypeError: 'tuple' object does not support item assignment (кортежи не поддерживают обращения по элементам
# исключение если внутри кортежа есть элемент список[]
print(immutable_var)
tuple[0][0]=30
tuple[0][1]=40
print(immutable_var) # в результате изменим содержимое списка внутри кортежа

list=["Aleks", 55, False]
mutable_list=list
print(mutable_list)
list[0]="Jack"
list[1]=35
print(mutable_list)