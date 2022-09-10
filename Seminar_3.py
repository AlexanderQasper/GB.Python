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
# import math
#
# array = [1.1, 1.2, 3.1, 5, 10.01]
# frac_array = []
#
# for i in range(len(array)):
#     frac_num, integral_num = math.modf(array[i])
#     if frac_num != 0:
#         frac_array.append(round(frac_num, 3))
#
# print(max(frac_array) - min(frac_array))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# 1 вариант
#print(bin(int(input()))[2:])

# 2 вариант
# num = int(input())
# binar = ''
# while num > 0:
#     binar += str(num % 2)
#     num //= 2
# print(binar)

# 5. Cоставьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = int(input('Введите число: ')) + 1

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(k)
print(get_fibonacci(k))
