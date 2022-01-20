# Реалізуй функцію combine_arrays, яка приймає 2 списки чисел (ls1 та ls2) 
# та повертає список чисел де result_list[i] це сума чисел ls1[i] та ls2[i].
# Примітки:
# Вхідні списки завжди однакового розміру.
# Приклади:
# combine_arrays([1, 2, 5], [3, 6, 1]) == [4, 8, 6]
# combine_arrays([1], [6]) == [7]
# combine_arrays([], []) == []

print('********* Start of programm *********')

def combine_lists(ls1: list, ls2: list) -> list:
        return [ls1[x]+ls2[x] for x in range(0, len(ls1))]

menuPoint=1
while menuPoint!='0':
    f_lst=[]
    s_lst=[]
    lst_len=int(input('Type len for your lists: '))
    for x in range(0, lst_len):
        f_lst.append(int(input(f'Type element {x} in FIRST LIST: ')))
    for x in range(0, lst_len):
        s_lst.append(int(input(f'Type element {x} in SECOND LIST: ')))
    print(combine_lists(f_lst, s_lst))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit