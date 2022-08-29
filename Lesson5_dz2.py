# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе число

while True:
    number_1 = int(input('введи первое число: '))
    action = input('введи действие (деление, умножение, сложение, разность): ')
    number_2 = int(input('введи второе число: '))

    if action == 'деление' or action == '/':
        print(f'{number_1}/{number_2} = {number_1 / number_2}')
    elif action == 'умножение' or action == '*':
        print(f'{number_1}*{number_2} = {number_1 * number_2}')
    elif action == 'сложение' or action == '+':
        print(f'{number_1}+{number_2} = {number_1 + number_2}')
    elif action == 'разность' or action == '-':
        print(f'{number_1}-{number_2} = {number_1 - number_2}')
    else:
        print('не такого действия')
        break







