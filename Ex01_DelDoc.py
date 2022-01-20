#Наш новий бос, як виявилося, просто ненавидить голосні літери, тому нам потрібно прибрати їх з усієї документації.
#Напиши функцію remove_vowels, яка приймає рядок document і повертає рядок, де усі голосні з document видалені.
#Голосними для цього завдання вважаються букви aeiouy в будь-якому регістрі.
#Приклади:
#remove_vowels('document') == 'dcmnt'
#remove_vowels('I like my boss') == ' lk m bss'
#remove_vowels('350 euro') == '350 r'

print('********* Start of programm *********')

def remove_vowels(document: str) -> str:
    return ''.join(i for i in document if i not in 'aeiouyAEIOUY')

menuPoint=1
while menuPoint!='0':

    print(remove_vowels(input('Print your string: ')))
    
    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit