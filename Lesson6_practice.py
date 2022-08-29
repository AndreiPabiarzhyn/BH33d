# # Пример как работает LIFO
# numbers = []
#
# for i in range(5):
#     numbers.append(i)
#     print(numbers)
#
# while numbers:
#     del numbers[-1]
#     print(numbers)

# # Пример как работает FIFO
# numbers = []
#
# for i in range(5):
#     numbers.append(i)
#     print(numbers)
#
# while numbers:
#     del numbers[0]
#     print(numbers)

# def is_palindrome(text:str) -> None:
#     text = text.lower().replace(' ', '')
#     return text == text[::-1]
#
# word = input()
# result = is_palindrome(word)
# print(result)

# пример возвращения не только булевской переменной, но и саму переменную
# def is_palindrome(text:str):
#     text = text.lower().replace(' ', '')
#     return text == text[::-1], text
#
# word = input()
# result = is_palindrome(word)
# print(result)

# аргументы со значением по умолчанию
def foo(a, b, *args):
        print(a, b, args)


foo(4, 45, 6, 7, 8, 9, 9, 6,)


