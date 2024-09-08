team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'

# использование %:
t_1 = "В команде %s, участников: %s!" % ('Мастера кода', team1_num)
t_2 = "В команде %s, участников: %s!" % ('Волшебники данных', team2_num)
t_all = "Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num)
print(t_1, t_2, t_all, sep="\n")
print()
# использование format():
sc_1 = "Команда {0} решила задач: {1}!".format('Мастера кода', score_1)
sc_2 = "Команда {0} решила задач: {1}!".format('Волшебники данных', score_2)
print(sc_1, sc_2, sep="\n")
t1_t = "{0} решили задачи за {1}c!".format('Мастера кода', team1_time)
t2_t = "{0} решили задачи за {1}c!".format('Волшебники данных', team2_time)
print(t1_t, t2_t, sep="\n")
print()
# использование f-строк:
sc_all = f'Команды решили {score_1} и {score_2} задач.'
print(sc_all)

challenge_result = ''
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(result)

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) % 2
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
