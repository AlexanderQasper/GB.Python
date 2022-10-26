from math import *


# 1. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


def distance_point(a, b, c, d):
    Ax, Ay, Bx, By = a, b, c, d

    distance = sqrt(((Ax - Bx) ** 2) + ((Ay - By) ** 2))
    return round(distance, 2)


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).


def place_dekart(x, y):
    try:
        if x > 0 and y > 0:
            return 1
        elif x < 0 and y > 0:
            return 2
        elif x < 0 and y < 0:
            return 3
        else:
            return 4
    except:
        return 'Ошибка!'


#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.


array = [1, 2, 3, 4, 5, 6]


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


print(type(multiple_arrays_index(array)) == list)
print(multiple_arrays_index(array))
