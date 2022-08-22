# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

# import collections

# result = collections.Counter(text)
# print(result)

text: str = input('введи текст: ')
print(text)
result: dict = dict((i, text.count(i)) for i in set(text))
print(result)

