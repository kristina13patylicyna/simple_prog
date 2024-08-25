import random
import string

print('ДОБРО ПОЖАЛОВАТЬ В ГЕНЕРАТОР ПАРОЛЕЙ!!!'.center(100, '_'))
count = int(input('ВВЕДИТЕ КОЛИЧЕСТВО ПАРОЛЕЙ ДЛЯ ГЕНЕРАЦИИ: '))
lenght = int(input('ВВЕДИТЕ ДЛИНУ ПАРОЛЯ: '))

print('ОТВЕТЬТЕ НА ВОПРОСЫ ДЛЯ ГЕНЕРАЦИИ ПАРОЛЯ...', 'ВЫ МОЖЕТЕ ОТВЕЧАТЬ ДА/НЕТ НЕ ЗАВИСИМО ОТ РЕГИСТРА БУКВ')

chars = ''

digits = None
while digits == None:
    user = input(f'ВКЛЮЧАТЬ ЛИ ЦИФРЫ ({string.digits}) В ПАРОЛЬ?: ').lower()
    if user == 'да':
        digits = True
        chars += string.digits
    elif user == 'нет':
        digits = False
    else:
        print('ПОПРОБУЙТЕ ЕЩЁ РАЗ')

up_letters = None
while up_letters == None:
    user = input(f'ВКЛЮЧАТЬ ЛИ ПРОПИСНЫЕ БУКВЫ ({string.ascii_uppercase}) В ПАРОЛЬ?: ').lower()
    if user == 'да':
        up_letters = True
        chars += string.ascii_uppercase
    elif user == 'нет':
        up_letters = False
    else:
        print('ПОПРОБУЙТЕ ЕЩЁ РАЗ')

low_letters = None
while low_letters == None:
    user = input(f'ВКЛЮЧАТЬ ЛИ СТРОЧНЫЕ БУКВЫ ({string.ascii_lowercase}) В ПАРОЛЬ?: ').lower()
    if user == 'да':
        low_letters = True
        chars += string.ascii_lowercase
    elif user == 'нет':
        low_letters = False
    else:
        print('ПОПРОБУЙТЕ ЕЩЁ РАЗ')

punctuation = None
while punctuation == None:
    user = input(f'ВКЛЮЧАТЬ ЛИ СИМВОЛЫ (!#$%&*+-=?@^_) В ПАРОЛЬ?: ').lower()
    if user == 'да':
        punctuation = True
        chars += '!#$%&*+-=?@^_'
    elif user == 'нет':
        punctuation = False
    else:
        print('ПОПРОБУЙТЕ ЕЩЁ РАЗ')

delete_symb = None
while delete_symb == None:
    user = input('ИСКЛЮЧИТЬ ЛИ СИМВОЛЫ (il1Lo0O) ИЗ ПАРОЛЯ?: ').lower()
    if user == 'да':
        delete_symb = True
        chars = set(chars) - set('il1Lo0O')
    elif user == 'нет':
        delete_symb = False
        chars = set(chars)
    else:
        print('ПОПРОБУЙТЕ ЕЩЁ РАЗ')

password = ''
for i in range(count):
    for j in range(lenght):
        password += random.choice(''.join(chars))
    print(password)
    password = ''
