# x = True
# y = False
# z = False
#
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# вводится слово. необхадимо определить, является ли оно полиндромом

# slovo = input().lower().replace(' ', '')
# razvorot = slovo[::-1]
# if razvorot in slovo:
#     print('yes')
# else:
#     print('no')

# вводится строка, вывести уникальные символы строки
# (которые встречаются один раз)

# stroka = input('введи предложение: ').lower()
# print(set(stroka))
#
# for i in set(stroka):
#     if stroka.count(i) == 1:
#         print(i)

# вводится числ, посчитать его факториал

# n = int(input('введи число: '))
# factorial = 1
#
# for i in range(2, n+1):
#     factorial = factorial*i
#
# print(factorial)

# пользователь вводит строку, переспрашивать ввод, пока не введет число
stroka = input('веди число: ')

while not stroka.isdigit():
    stroka = input('веди число: ')



