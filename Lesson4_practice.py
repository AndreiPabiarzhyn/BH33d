# Пользователь вводит число N с клавиатуры
# посчитать сумму чисел от 1 до N

n:int = int(input('введи число '))

mnoghestvo:list =[i for i in range(1, n+1)]
print(mnoghestvo)
print(sum(mnoghestvo))



