# Вывести первые N цисел кратные M и больше K
lower = int(input('ввести нижний жиапозон: '))
upper = int(input('ввести нижний жиапозон: '))
m = int(input('ввести делитель: '))
k = int(input('введи число: '))

for i in range(lower,upper+1):
    if i%m == 0 and i>k:
        print(i)
