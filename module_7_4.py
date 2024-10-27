def num(team1_num, team2_num):
    print('В команде Волщебники данных %s участников: %s !' % (team1_num, team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))


# Использование format:


def time(team1, score1, team1_time):
    print('Команда {} решила задач: {}!'.format(team1, score1))
    print('{} решили задачи за {} cек. !'.format(team1, team1_time))


# Использование f-строк:

def challenge_result(tasks_total, time_avg):
    print(f'Команды решили {score1} и {score2} задач')
    if score1 > score2 or score1 == score2 and team1_time > team2_time:
        result = f'Результат битвы: победа команды {team1} !'
    elif score1 < score2 or score1 == score2 and team1_time < team2_time:
        result = f'Результат битвы: победа команды {team1} !'
    else:
        result = f'Ничья!'

    print(result)
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')


score1 = 42
score2 = 40
team1 = 'Волщебники данных'
team2 = 'Мастера кода'
time_avg = 45.2
team1_time = 1552.512
team2_time = 2153.31451
team1_num = 5
team2_num = 6
tasks_total = score1 + score2
num(team1_num, team2_num)
time(team1, score1, team1_time)
challenge_result(tasks_total, time_avg)