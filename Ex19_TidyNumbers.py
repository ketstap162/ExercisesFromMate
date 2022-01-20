# Все в порядку! Принаймні так має бути :)
# Давай перевіримо чи всі наші номери охайні і всі цифри стоять у правильному порядку. 
# Отже, нам треба переконатися що всі цифри у наших номерах розташовані у неспадаючій послідовності.
# Оголосимо функцію is_tidy яка приймає number у якості параметра та має виводити результат True якщо цифри у неспадаючій послідовності, або False якщо ні.
# Примітка Вхідні значення завжди додатні.
# Приклади:
# is_tidy(12) == True Цифри { 1, 2 } розташовані у неспадаючій послідовності, тобто 1 <= 2.
# is_tidy(32) == False Цифри { 3, 2 } розташовані в спадаючій послідовності, тобто 3 > 2.
# is_tidy(1024) == False Цифри { 1, 0, 2, 4 } розташовані в спадаючій послідовності, оскільки 0 < 1.
# is_tidy(3445) == True Цифри { 3, 4, 4, 5 } розташовані в неспадаючій послідовності, оскільки 4 <= 4.
# is_tidy(13579) == True Цифри { 1, 3, 5, 7, 9 } розташовані в зростаючій послідовності.

print('********* Start of programm *********')

def is_tidy(number: int) -> bool:
    ls_numb=[int(x) for x in str(number)]
    ls_check=[]
    for x in range(1, len(ls_numb)):
        if ls_numb[x]>=ls_numb[x-1]:
            ls_check.append(True)
        else:
            ls_check.append(False)
    return all(ls_check)

menuPoint=1
while menuPoint!='0':

    print(is_tidy(int(input('Type your number: '))))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit