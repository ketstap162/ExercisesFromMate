# Створіть функцію check_number, яка перевіряє число на три різні властивості:
# Це позитивне число?
# Це парне число?
# Це число кратне 10?
# Функція check_number повинна повернути список з результатами перевірок у вигляді булевих значень.
# Число завжди має бути цілим.
# Приклад:
# check_number(3) == [True, False, False]
# check_number(10) == [True, True, True]
# check_number(0) == [False, True, True]
# check_number(-1) == [False, False, False]

print('********* Start of programm *********')

def check_number(number: int) -> list:
    checking=[None,None,None]
    if number>0:
        checking[0]=True
    else:
        checking[0]=False
    if number%2==0:
        checking[1]=True
    else:
        checking[1]=False
    if number%10==0:
        checking[2]=True
    else:
        checking[2]=False
    return checking

menuPoint=1
while menuPoint!='0':

    print(check_number(int(input('Print your int number: '))))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit