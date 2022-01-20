# Ну що, коли всі процеси налаштовано, потрібно ставити перед собою правильні цілі. 
# Наші роботи найкращі на ринку, тому потрібно нарощувати оберти і збільшувати обсяги виробництва.
# Давай напишемо функцію get_plan, яка складе план виробництва на задану кількість місяців months. 
# Зараз ми виготовляємо current_production роботів на місяць і хочемо, щоб щомісяця це число зростало на заданий відсоток percent.
# Якщо число роботів на ітерації виявилось не цілим, округли його вниз (використай функцію floor з модуля math). 
# В решті отримаємо список з цілями на найближчі місяці.
# Приклади:
# get_plan(1000, 6, 30) == [1300, 1690, 2197, 2856, 3712, 4825]
# get_plan(500, 3, 50) == [750, 1125, 1687]

print('********* Start of programm *********')

import math

def get_plan(current_production: int, month: int, percent: int):
    lst=[]
    for _ in range(1, month+1):
        current_production=math.floor(current_production*((percent+100)/100))
        lst.append(current_production)
    return lst

menuPoint=1
while menuPoint!='0':

    typed_prod=int(input(f'Type count of current production: '))
    typed_month=int(input(f'Type count of months: '))
    typed_percent=int(input(f'Type count of percent: '))
    print(get_plan(typed_prod, typed_month, typed_percent))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit