# Псс... Ми тут придумали цікаву ідею для бізнесу. У світі є багато речей, які складаються з кількох слів. 
# Ми можемо створити суперпрограму make_abbr, яка буде повертати для них абревіатури!!! Такого точно ще ніхто не робив!
# Допоможеш нам? Ти в долі. Як тільки це почне приносити нам прибутки, ми перерахуємо кошти тобі. Точно-точно. Ух. Заживемо!
# Ти можеш розраховувати, що назва складається виключно з букв, а слова розділені одним пробілом.
# Приклади:
# make_abbr('national aeronautics space administration') == 'NASA'
# make_abbr('central processing unit') == 'CPU'
# make_abbr('simplified molecular input line entry specification') == 'SMILES'

print('********* Start of programm *********')

def make_abbr(words: str) -> str:
    return ''.join(x for x in words.title() if x.isupper())

menuPoint=1
while menuPoint!='0':

    print(make_abbr(input('Print your string: ')))
    
    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit