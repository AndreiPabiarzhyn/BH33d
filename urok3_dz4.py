# Пользователь вводит три числа
# Сказать сколько из них положительных и сколько отрительных

negative: int = 0
positiv: int = 0
list: list = []

# for i in range(3):
#     vvod: int = int(input('введи число: '))
#     if vvod>0 :
#         positiv += 1
#     else:
#         negative +=1
# print(positiv, ' положительных чисел')
# print(negative, ' отрицательных чисел')

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print((a > 0) + (b > 0) + (c > 0), 'положительные числа')
print((a < 0) + (b < 0) + (c < 0), 'отрицательные числа')
