def __getage():
    x = int(input())
    if 0 <= x <= 44:
        print('Молодой человек')
    elif 45 <= x <= 59:
        print('Средний возраст')
    elif 60 <= x <= 74:
        print('Пожилой человек')
    elif 75 <= x <= 90:
        print('Старческий возраст')
    elif x > 90:
        print('Долгодитель')
