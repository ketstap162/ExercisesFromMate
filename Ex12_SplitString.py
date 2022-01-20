# Напиши функцію split_string, яка приймає рядок і повертає список рядків з двох символів. 
# Якщо рядок містить непарну кількість символів, тоді другий символ потрібно замінити на підкреслення ("_").
# Приклад:
# split_string('abc') == ['ab', 'c_']
# split_string('abcdef') == ['ab', 'cd', 'ef']

print('********* Start of programm *********')

def split_string(string: str) -> list:
    return [i+j for i, j in zip(string[::2], string[1::2]+'_')]

menuPoint=1
while menuPoint!='0':

    print(split_string(input('Type your sring: ')))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit