# Пользователь вводит три числа
# Сказать сколько из них положительных и сколько отрительных

negative: int = 0
positiv: int = 0

for i in range(3):
    vvod: int = int(input('введи число: '))
    if vvod>0 :
        positiv += 1
    else:
        negative +=1
print(positiv, ' положительных чисел')
print(negative, ' отрицательных чисел')