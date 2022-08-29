# Дан список строк, наобходимо реализовать пагинатор

paginator = [1, 2, 3, 4, 5]
i = 0

while True:
    vvod = input('введи > или <: ')
    if vvod == '>':
        i = i + 1
        if i > len(paginator)-1:
            i = 0
        print(paginator[i])
    if vvod == '<':
        i = i - 1
        if i < 0:
            i = len(paginator)-1
        print(paginator[i])
