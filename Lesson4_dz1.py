# Заполнить список степенями числа 2 (от 2^1 до 2^n).
step: int = int(input('введи число: '))
list_1: list = [2**i for i in range(1, step+1)]
print(list_1)
