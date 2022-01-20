# Ми удосконалили нашу програму для збору статистики з вебінарів. 
# Тепер після збору статистики, вона відправляє дані на сервер у вигляді рядка 111001010111011, де 1 - це студент, який зрозумів тему, а 0 - відповідно, ні.
# Було б корисно розуміти скільки відсотків групи засвоїли матеріал, це покаже наскільки вебінар був ефективний.
# Створи функцію get_success_rate, яка приймає рядок statistic та повертає відсоток студентів, які зрозуміли матеріал,
# округляючи до найближчого цілого (використай round(result) для округления).
# Приклади:
# get_success_rate('11100') == 60
# get_success_rate('1100') == 50
# get_success_rate('000000') == 0
# get_success_rate('11111') == 100
# get_success_rate('') == 0

print('********* Start of programm *********')

def get_success_rate(statistics: str) -> int:
    return round(sum(int(x) for x in statistics if int(x)==1)/len(statistics)*100)

menuPoint=1
while menuPoint!='0':

    print(get_success_rate(input('Enter a number of zeros and ones:\n')))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit