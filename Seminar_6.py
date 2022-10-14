# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# ДО
# number = int(input())
# sum = 0
# while number > 0:
#     digit = number % 10
#     sum += digit
#     number //= 10
# print(sum)
#
# # ПОСЛЕ
# print(*[sum(int(i) for i in input() if i.isnumeric())])

# 2. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# ДО
# array = [2, 13, 105, 4, 12, 7, 54, 101, 205, 1, 2]
# summa = 0
# for i in range(1, len(array), 2):
#     summa += array[i]
# print(summa)
#
# # ПОСЛЕ
# print(sum(v for i, v in enumerate(array) if i % 2))
