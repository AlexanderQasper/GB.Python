# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# import copy
#
#
# class Matrix:
#
#     # Перегружаем метод инициализации в конструктор класса. Если правильно понял, класс матрица при вызове сразу
#     # получают сущнность мартицы
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     # Вмешиваемся в принты, создаём пустую строку и добавляем циклом в неё числа матрицы, переводя их в строку и
#     # используем метод джоин + переход на новую строку для красоты
#     def __str__(self):
#         s = ''
#         for i in range(len(self.matrix)):
#             s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
#         return s
#
#     # Перехватываем встроенный функционал сложения, прописывая, что и как нужно складывать. Вложенным циклом, как обычныую функцию сложения матрицы
#     def __add__(self, other):
#         if len(self.matrix) != len(other.matrix):
#             return None
#         res = copy.deepcopy(self.matrix)
#         for i in range(len(self.matrix)):
#             for k in range(len(self.matrix[i])):
#                 res[i][k] = self.matrix[i][k] + other.matrix[i][k]
#         return Matrix(res)
#
#
# l1 = [[1, 2, 4], [3, 4, 5], [5, 6, 6]]
# l2 = [[11, 21, 41], [31, 41, 51], [51, 61, 61]]
# matrix1 = Matrix(l1)
# matrix2 = Matrix(l2)
# print(matrix1)
# print(matrix2)
# end_matrix = matrix1 + matrix2
# print(end_matrix)

# 2 Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     # При инициализации говорим, что сразу, при вызове будем передавать параметр
#     def __init__(self, param):
#         self.param = param
#
#     # Декоратором будем проверять, что дальше ОБЯЗАТЕЛЬНО этот метод будет изменён
#     @abstractmethod
#     def expense(self):
#         pass
#
#     def __str__(self):
#         return str(self.param)
#
#
# class Coat(Clothes):
#
#     @property
#     def expense(self):
#         return self.param / 6.5 + 0.5
#
#
# class Suit(Clothes):
#
#     @property
#     def expense(self):
#         return self.param * 2 + 0.3
#
#
# a = Coat(52)
# b = Suit(1.80)
# print(a)
# print(a.expense)
# print(b.expense)

# Задание 3.
# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка (Cell).
# В его конструкторе инициализировать параметр (quantity),
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()),
# вычитание (sub()),
# умножение (mul()),
# деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.simbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for k in range(1,count+1):
                print(self.simbol, end ='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end = '')



a = Cell(5)
b = Cell(10)
c = Cell(3)
d = Cell(2)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)