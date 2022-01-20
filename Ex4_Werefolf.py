# До нас дійшла інформація, що перевертні можуть бути небезпечними для людей. Ми ще не знаємо чому, але ігнорувати цю інформацію не можемо.
# Треба якомога швидше почати виявляти перевертнів. Пропонуємо для початку за ціль target брати слова і речення. 
# Вони далеко не втечуть в разі чого. Як ми зрозуміли, серед слів і речень перевертні - це ті слова, 
# які читаються в обох напрямках однаково і при цьому ігнорують пробіли і розділові знаки.
# Напиши, будь ласка, функцію is_werewolf, яка отримує рядок target і повертає True, якщо це перевертень.
# Примітка: target може містити латинські літери (і великі, і малі), пробіли та розділові знаки.
# Приклади:
# is_werewolf('rotator') == True # rotator --> rotator
# is_werewolf('home') == False # home --> emoh
# is_werewolf('racecar') == True
# is_werewolf('red rum sir is murder') == True
# is_werewolf('eva, can I see bees in a cave') == True

print('********* Start of programm *********')

def is_werewolf(target: str) -> bool:
    for x in [' ', '.', ',', '!', ':', ';', '"', '\'', '(', ')', '[', ']', '{', '}','-','_','?']:
        while target.find(x)!=-1:
            target=target.replace(x,'')
    return target.lower()==target[::-1].lower()

menuPoint=1
while menuPoint!='0':

    print(is_werewolf(input('Print your string: ')))
    
    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit