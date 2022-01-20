# Реалізуй функцію get_arrays_sum, яка приймає два списки чисел однакової довжини, 
# та повертає суму усіх елементів цих списків.
# Приклад:
# get_arrays_sum([1, 2], [3, 4]) == 10  # 1 + 2 + 3 + 4 = 10
# get_arrays_sum([], []) == 0

print('********* Start of programm *********')

def get_lists_sum(ls1: list, ls2: list) -> int:
    return sum(ls1+ls2)

menuPoint=1
while menuPoint!='0':
    f_lst=[]
    s_lst=[]
    f_len=int(input('Print len for fisrt list: '))
    for x in range(0, f_len):
        f_lst.append(int(input(f'Element {x} in FIRST LIST equal: ')))
    s_len=int(input('Print len for second list: '))
    for x in range(0, s_len):
        s_lst.append(int(input(f'Element {x} in SECOND LIST equal: ')))
    print(get_lists_sum(f_lst, s_lst))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit