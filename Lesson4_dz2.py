# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

# import collections

# results = collections.Counter(text)
# print(results)

text: str = input('введи текст: ')
print(text)
rezult: dict = dict((i, text.count(i)) for i in set(text))
print(rezult)

