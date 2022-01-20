# Напиши функцію parity_checker, яка, за допомогою функції input читає число та виводить рядок "Even", якщо число парне, та рядок "Odd", якщо число непарне. 
# Обов'язково передай у функцію input повідомлення "What number do you want to check?", щоб користувачу було зрозуміло, яку інформацію потрібно ввести.
# Підказка: функція input завжди повертає рядок. Наприклад, якщо користувач введе число 4, то input поверне рядок "4". 
# Щоб привести рядок до числа використай функцію int.
# Приклад:
# age = int(input("How old are you?"))
# Користувач вводить "21"
# print(type(age)) # На екран виводиться "<class 'int'>"

print('********* Start of programm *********')

def parity_checker() -> None:
    numb=int(input('What number do you want to check?\n'))
    if numb%2:
        print('Odd')
    else:
        print('Even')

menuPoint=1
while menuPoint!='0':

    parity_checker()
    
    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit