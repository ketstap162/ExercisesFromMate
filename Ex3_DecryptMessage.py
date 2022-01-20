# Нещодавно археологи знайшли старі записи древньої цивілізації. 
# Виявляється у них вже була розвинена писемність і була своя мова. Але найкрутіше з цього всього те, що говорили вони просто задом наперед. 
# Археологи відправили знахідку нам на розшифровку.
# Давай розшифруємо decrypt_message послання message древньої цивілізації нащадкам!!!
# Приклади:
# decrypt_message('!!!reeb gniknird ekil eW') == 'We like drinking beer!!!'
# decrypt_message('0202 ni eb lliw cimednap surivanoroc A') == 'A coronavirus pandemic will be in 2020'

print('********* Start of programm *********')

def decrypt_message(message: str) -> str:
    return message[::-1]

menuPoint=1
while menuPoint!='0':

    print(decrypt_message(input('Print your string: ')))
    
    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit