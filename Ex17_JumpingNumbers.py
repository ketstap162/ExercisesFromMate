# Реалізуй функцію is_jumping, яка приймає число number та повертає рядок JUMPING,
# якщо кожна цифра в числі відрізняється від сусідньої на 1. Якщо умова не виконується - рядок NOT JUMPING.
# Примітки:
# Вхідне число завжди додатнє
# Різниця між 9 та 0 не розцінюється як 1
# Всі числа, які складаються із однієї цифри - JUMPING
# Приклади:
# is_jumping(9) == 'JUMPING'
# It's single-digit number
# is_jumping(79) == 'NOT JUMPING'
# Adjacent digits don't differ by 1
# is_jumping(23454) == 'JUMPING'
# Adjacent digits differ by 1

print('********* Start of programm *********')

def is_jumping(number: int) -> str:
    ls=[int(x) for x in str(number)]
    ls1=[]
    if len(ls)>1:
        for x in range(1, len(ls)):
            if ls[x]-ls[x-1]==1 or ls[x]-ls[x-1]==-1:
               ls1.append(True)
            else:
               ls1.append(False)
        if all(ls1):
            return 'JUMPING'
        else:
            return 'NOT JUMPING'
    else:
        return 'JUMPING'

menuPoint=1
while menuPoint!='0':

    print(is_jumping(int(input('Type int number: '))))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit