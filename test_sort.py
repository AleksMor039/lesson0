from function_sort import insertion_sort, bubble_sort, selection_sort
from speed_functions import func

data_1 = [23, 7, 89, 5]
data_2 = [6, 18, 4, 3, 2, 10, 34]
data_3 = [90, 80, 60, 44, 33, 11, 22, 55, 66]



print(insertion_sort(data_1))
print(insertion_sort(data_2))
print(insertion_sort(data_3))
print(func(insertion_sort(sum(data_1 + data_2 + data_3))))


# print(bubble_sort(data_1))
# print(bubble_sort(data_2))
# print(bubble_sort(data_3))
# print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
# print(selection_sort(data_1))
# print(selection_sort(data_2))
# print(selection_sort(data_3))
# print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))