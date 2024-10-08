from random import shuffle, choice

def magic():
    s = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова',\
        'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже',\
        'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', \
        'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',\
        'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',\
        'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
    shuffle(s)
    return choice(s)


print('Приветствую, странник этой бренной земли. Ответь мне на один вопрос. Как твоё имя?')
user_name = input()
print(f'Привет, {user_name}! Рад тебя чувствовать. ')
print()

while True:
    print(f'{user_name}, задайте свой вопрос...')
    question = input()
    print(magic())

    print('Желаете задать ещё вопрос? да/нет')
    ans_us = input()
    if ans_us == 'нет':
        print('Всего доброго, надеюсь я ответил на ваши вопросы')
        break
    elif ans_us == 'да':
        continue
    else:
        print('Я вас не понимаю...')
        print('Приходите позже')
        break


