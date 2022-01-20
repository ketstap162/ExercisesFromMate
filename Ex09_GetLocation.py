# Наші інженери зараз шукають баг, який змушує роботів винищувати людство...
# А ми поки випустимо оновлення. Раніше ми навчили роботів розуміти команди і перетворювати напрямок руху в правильний сигнал:
# 'forward' в x + 0 та y + 1
# 'back' в x + 0 та y - 1
# 'right' в x + 1 та y + 0
# 'left' в x - 1 та y + 0
# Було б чудово, якби робот знав, де він зараз знаходиться навіть без GPS.
# Напиши функцію get_location, яка приймає список початкових координат coordinates (у вигляді [x, y]) 
# та список історії команд commands, і повертає список кінцевих координат робота в тому ж форматі ([x, y]).
# Наприклад:
# coordinates = [2, 1]
# commands = ['left', 'back', 'back']
# Координати після першої команди: [1, 1] # 1 крок вліво
# Координати після другої команди: [1, 0] # 1 крок назад
# Координати після третьої команди: [1, -1] # 1 крок назад
# Результатом буде [1, -1]
# Інші приклади:
# get_location([0, 0], ['forward', 'right']) == [1, 1]
# get_location([2, 3], ['back', 'back', 'back', 'right']) == [3, 0]
# get_location([0, 5], ['back', 'back', 'back', 'right', 'left', 'forward']) == [0, 3]

print('********* Start of programm *********')

def get_location(coordinates: list, commands: list) -> list:
    for s in commands:
        if s=='forward':
            coordinates[1]+=1
        elif s=='back':
            coordinates[1]-=1
        elif s=='right':
            coordinates[0]+=1
        elif s=='left':
            coordinates[0]-=1
    return coordinates

menuPoint=1
while menuPoint!='0':

    x=int(input('Coordination. Type X: '))
    y=int(input('Coordination. Type Y: '))
    com_list=[]
    com_list_range=int(input('Type range of command list: '))
    for l in range(0, com_list_range):
        com_list.append(input(f'Command {x+1}. Type <forward>, <back>, <right> or <left>: '))
    print(get_location([x, y], com_list))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit