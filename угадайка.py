from random import randint

num = randint(1, 100)
print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    if (n.isdigit() == True) and ((int(n) >= 1) and (int(n) <= 100)):
        return True
    else:
        return False

#print(is_valid('50'))

while True:
    user_input = input()
    if is_valid(user_input) == True:
        user_input = int(user_input)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        user_input = int(input())

    if user_input > num :
        print('Слишком много, попробуйте еще раз')
    if user_input < num:
        print ('Слишком мало, попробуйте еще раз')
    if user_input == num:
        print('Вы угадали, поздравляем!')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

