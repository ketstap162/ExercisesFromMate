# Функція is_special_number приймає число, та повинна визначити, чи особливе воно чи ні. 
# Число називається особливим, якщо воно включає в себе лише 0, 1, 2, 3, 4 або 5.
# Функція is_special_number повинна повертати рядок 'Special!!', якщо число особливе, та 'NOT!!', якщо воно таким не є.
# Примітки:
# Число, яке передається у функцію є додатнім (n > 0).
# Всі одноцифрові числа в інтервалі [0:5] вважаються особливими числами.
# Приклади:
# is_special_number(2) == 'Special!!'
# 2 - це одноцифрове число в інтервалі [0:5].
# is_special_number(9) == 'NOT!!'
# хоча 9 - це одноцифрове число, але воно не знаходиться в інтервалі [0:5].
# is_special_number(23) == 'Special!!'
# всі цифри числа 23 знаходяться у інтервалі [0:5].
# is_special_number(39) == 'NOT!!'
# хоча і є число 3, яке знаходиться у інтервалі, але друге число (9) у ньому не знаходиться (кожна цифра має знаходитись в інтервалі [0:5]).

print('********* Start of programm *********')

def is_special_number(number: int) -> str:
    checking=[0,1,2,3,4,5]
    ls_numb=[int(x) for x in str(number)]
    ls_check=[]
    for x in ls_numb:
        if x in checking:
            ls_check.append(True)
        else:
            ls_check.append(False)
    if all(ls_check):
        return 'Special!!'
    else:
        return 'NOT!!'

menuPoint=1
while menuPoint!='0':

    print(is_special_number(int(input('Type your number: '))))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit