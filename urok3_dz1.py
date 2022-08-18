# Пользователь вводит предлложение, заменить все пробелы на "-"
# двумя способами

# вводные данные
stroka: str = input(" введи предложение").strip()

# решение1
sposob1: str = stroka.replace(' ', '-')

# Решение 2
sposob2:list = stroka.split()
sposob2:str = '-'.join(sposob2)

# вывод результата
print(sposob1)
print(sposob2)