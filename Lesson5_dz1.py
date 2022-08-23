# Дан список чисел, отсортировать его по возрастанию
# без использования sort и sorted
spisok = [1, 4, 6, 8, 0, 3, 55, 58, 32, 45, 78, 76]
n = 1

while n < len(spisok):
    for i in range(len(spisok)-n):
        if spisok[i] > spisok[i+1]:
            spisok[i], spisok[i+1] = spisok[i+1], spisok[i]
    n += 1
print(spisok)




