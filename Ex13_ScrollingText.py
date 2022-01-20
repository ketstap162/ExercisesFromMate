# Створи функцію scrolling_text, яка приймає рядок як параметр, послідовно переставляє всі символи у рядку з нульового індексу до останнього 
# і повертає список з усіма отриманими комбінаціями в верхньому регістрі.
# Приклад
# scrolling_text("robot")
# Повертає:
# [ "ROBOT",
#   "OBOTR",
#   "BOTRO",
#   "OTROB",
#   "TROBO" ]

print('********* Start of programm *********')

def scrolling_text(string: str) -> list:
    return [string[x::].upper()+string[:x].upper() for x in range(0, len(string))]

menuPoint=1
while menuPoint!='0':

    print(scrolling_text(input('Type your string: ')))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit