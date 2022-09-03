# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input("Введите номер дня недели от 1 до 7: "))
#
# if 1 <= day <= 7:
#     if day in [6, 7]:
#         print("да")
#     else:
#         print("нет")
# else:
#     print("Ошибка! Введите число8 от 1 до 7 включительно!")

# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x, y = int(input("Введите х: ")), int(input("Введите y: "))
#
#
# def place_dekart(x, y):
#     if x > 0 and y > 0:
#         return 1
#     elif x < 0 and y > 0:
#         return 2
#     elif x < 0 and y < 0:
#         return 3
#     else:
#         return 4
#
#
# print(f"Номер четверти на координатной плоскости: {place_dekart(x, y)}")

# 3. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a
#
#
# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result
#
#
# statement = inputNumbers(3)
#
# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")

# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# quart_number = int(input())
#
#
# if quart_number in [1, 2, 3, 4]:
#     if quart_number == 1:
#         print("Значения координат точки: х ∈ [1, ∞), y ∈ [1, ∞)")
#     elif quart_number == 2:
#         print("Значения координат точки: х ∈ [-1, -∞), y ∈ [1, ∞)")
#     elif quart_number == 3:
#         print("Значения координат точки: х ∈ [-1, -∞), y ∈ [-1, -∞)")
#     elif quart_number == 4:
#         print("Значения координат точки: х ∈ [1, ∞), y ∈ [-1, -∞)")
# else:
#     print("Ошибка! Введите число от 1 до 4")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from math import *

Ax, Ay, Bx, By = int(input("Точка А, х: ")), int(input("Точка А, у: ")), int(input("Точка B, х: ")), int(
    input("Точка B, y: "))

distance = sqrt(((Ax - Bx) ** 2) + ((Ay - By) ** 2))
print(int(distance * 100) / 100)
