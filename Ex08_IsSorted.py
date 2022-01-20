# Поки в нас достатньо роботів, давайте навчимо їх сортувати коробки на складі. Всі коробки мають номери, а роботи вчаться сортувати їх в порядку зростання.
# Але сортування — справа нелегка, іноді трапляються помилки. Тому нам поки доведеться перевіряти, чи правильно робот відсортував коробки.
# Напиши функцію is_sorted, яка отримує список номерів і повертає True або False. (Номери - це завжди числа, але вони можуть повторюватись)
# Приклади:
# is_sorted([1, 2, 3, 4, 5]) == True
# is_sorted([0, 1, 1, 1, 2]) == True
# is_sorted([1, 5, 7]) == True
# is_sorted([1, 2, 11]) == True
# is_sorted([5]) == True
# is_sorted([]) == True
# is_sorted([0, 3, 1, 2, 2, 2]) == False
# is_sorted([1, 11, 2]) == False
# is_sorted([5, 3]) == False

print('********* Start of programm *********')

def is_sorted(box_numbers: list) -> bool:
    return box_numbers==sorted(box_numbers)

menuPoint=1
while menuPoint!='0':

    lst=[]
    count_list=int(input('Type count of elements on list: '))
    for x in range (0, count_list):
        lst.append(int(input(f'Enter {x} element: ')))
    print(is_sorted(lst))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit