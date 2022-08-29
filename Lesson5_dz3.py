#Вывести четные числа от 2 до N по 5 в строку
n = int(input('введи число: '))
i = 2

while i <= n:
    if i%2 == 0:
        if i%5 == 0:
            print(i)
        else:
            print(i, end=', ')
    i += 1
