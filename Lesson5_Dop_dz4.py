# Дан список чисел, отсортировать его по возрастанию
# без использования sort и sorted
spisok = [1, 5, 76, 23, 645, 33, 78]
print(spisok[2])

for _ in spisok:
    for i in range(len(spisok)-1):
        if spisok[i] > spisok[i+1]:
            spisok[i], spisok[i+1] = spisok[i+1], spisok[i]
print(spisok)

