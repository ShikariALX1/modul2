import random


def pass_(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if ((i + j) == n or n % (i + j) == 0):
                result += str(i) + '+' + str(j) + ' '
    result = result.replace('+', '')
    result = result.replace(' ', '')
    return result


while True:
    pole_1 = random.choice(range(3, 21))
    pole_2 = pass_(int(pole_1))
    print(f'Пароль: {pole_1} {pole_2}')
    break
