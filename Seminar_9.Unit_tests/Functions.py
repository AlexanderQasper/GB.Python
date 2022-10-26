from math import *


# 1. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D
# пространстве.


def distance_point(a, b, c, d):
    Ax, Ay, Bx, By = a, b, c, d

    distance = sqrt(((Ax - Bx) ** 2) + ((Ay - By) ** 2))
    return round(distance, 2)


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).


def place_dekart(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


# 3. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def multiple_arrays_index(start_array):
    end_array = []
    if len(start_array) % 2 == 0:
        for i in range(1, (len(start_array) // 2) + 1):
            end_array.append(start_array[i - 1] * start_array[-i])
        return end_array
    else:
        for i in range(1, (len(start_array) // 2) + 1):
            end_array.append(start_array[i - 1] * start_array[-i])
        end_array.append((start_array[floor(len(start_array) / 2)]) ** 2)
        return end_array


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def into_binar(x):
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x //= 2
    return n


# 5. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def multipliers_num(x):
    number = x
    multipliers = []

    for i in range(1, number // 2 + 1):
        if number % i == 0:
            multipliers.append(i)
    return multipliers


# 6. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def delete_str(text):
    end_text = list(filter(lambda x: 'абв' not in x, text.split()))
    return end_text


# 7. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
#максимальным и минимальным значением дробной части элементов.
def min_and_max(array):
    frac_array = []
    for i in range(len(array)):
        frac_num, integral_num = modf(array[i])
        if frac_num != 0:
            frac_array.append(round(frac_num, 3))

    return max(frac_array) - min(frac_array)

#print(min_and_max([1.1, 1.2, 3.1, 5, 10.01]))
