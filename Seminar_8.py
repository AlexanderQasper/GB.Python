# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
import copy


class Matrix:

    # Перегружаем метод инициализации в конструктор класса. Если правильно понял, класс матрица при вызове сразу
    # получают сущнность мартицы
    def __init__(self, matrix):
        self.matrix = matrix

    # Вмешиваемся в принты, создаём пустую строку и добавляем циклом в неё числа матрицы, переводя их в строку и
    # используем метод джоин + переход на новую строку для красоты
    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    # Перехватываем встроенный функционал сложения, прописывая, что и как нужно складывать. Вложенным циклом, как обычныую функцию сложения матрицы
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


l1 = [[1, 2, 4], [3, 4, 5], [5, 6, 6]]
l2 = [[11, 21, 41], [31, 41, 51], [51, 61, 61]]
matrix1 = Matrix(l1)
matrix2 = Matrix(l2)
print(matrix1)
print(matrix2)
end_matrix = matrix1 + matrix2
print(end_matrix)
