# Пользователь вводит 3 числа, найти среднее арифметическое с точностью 3
summa:int= 0

for i inrange(3):
    vvod_chisla:int=int(input("введи число: "))
    summa = summa + vvod_chisla
otvet:float= summa/3
print(round(otvet, 3))