from math import *


# 1. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


def distance_point(a, b, c, d):
    Ax, Ay, Bx, By = a, b, c, d

    distance = sqrt(((Ax - Bx) ** 2) + ((Ay - By) ** 2))
    return round(distance, 2)


print(distance_point(2, 3, 2, 8))
