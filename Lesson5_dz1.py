# Вывести первые N цисел кратные M и больше K
lower = int(input('ввести нижний диапозон: '))
upper = int(input('ввести верхний диапозон: '))
m = int(input('ввести делитель: '))
k = int(input('введи число: '))
print([i for i in range(lower, upper+1)])

for i in range(lower, upper+1):
    if i%m == 0 and i>k:
        print(i)
