# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# array = [2, 13, 105, 4, 12, 7, 54, 101, 205, 1, 2]
# summa = 0
# for i in range(1, len(array), 2):
#     summa += array[i]
#
# print(summa)

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Заморочился через функцию...

# import math
#
# array = [int(i) for i in input('Введите числа массива через пробел: ').split()]
#
#
# def miltiple_arrays_index(start_array):
#     end_array = []
#     if len(start_array) % 2 == 0:
#         for i in range(1, (len(start_array) // 2) + 1):
#             end_array.append(start_array[i - 1] * start_array[-i])
#         return end_array
#     else:
#         for i in range(1, (len(start_array) // 2) + 1):
#             end_array.append(start_array[i - 1] * start_array[-i])
#         end_array.append((start_array[math.floor(len(start_array) / 2)]) ** 2)
#         return end_array
#
#
# print(miltiple_arrays_index(array))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

