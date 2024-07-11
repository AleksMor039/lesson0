number_of_completed_tasks=12 #количество выполненных задач
number_of_hours_spent=1.5 # количество затраченных часов
course_name='Python' # название курса
time_for_one_task=(number_of_hours_spent / number_of_completed_tasks)   # время на одно задание
print("Курс:",course_name, "," "всего задач:" ,number_of_completed_tasks, "," "затрачено часов:", number_of_hours_spent, "," "среднее время выполнения", time_for_one_task)
