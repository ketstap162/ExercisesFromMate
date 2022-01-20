# Перша партія роботів готова, тепер їх треба перевірити. 
# Всі роботи унікальні, тому в кожного своя швидкість руху. Помилка в коді? Можливо. Але зараз не до цього. 
# Треба визначити найнижчу, найвищу та середню швидкість наших роботів.
# Наш сервер приймає список швидкостей роботів test_results, пропускає його через функцію get_speed_statistic
# і повертає статистику у вигляді списку, де
# перший елемент - це мінімальна швидкість
# другий - максимальна
# третій - середня швидкість, округлена вниз (використай функцію floor)
# Приклади:
# get_speed_statistic([10, 10, 11, 9, 12, 8]) == [8, 12, 10]
# get_speed_statistic([10]) == [10, 10, 10]
# get_speed_statistic([]) == [0, 0, 0]
# get_speed_statistic([8, 9, 9, 9]) == [8, 9, 8]
# get_speed_statistic([5]) == [5, 5, 5]

print('********* Start of programm *********')

import math

def get_speed_statistic(test_results: list) -> list:
    if test_results:
        return [min(test_results), max(test_results), math.floor(sum(test_results)/len(test_results))]
    else:
        return [0,0,0]

menuPoint=1
while menuPoint!='0':

    my_lst=[]
    my_count=int(input('Type count of robots: '))
    for x in range (0, my_count):
        my_lst.append(int(input(f'Robot N{x+1}. Speed: ')))
    print(get_speed_statistic(my_lst))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit