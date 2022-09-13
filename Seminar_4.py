# 1. Вычислить число c заданной точностью d

# d = float(input('Введите степень точности в формате 0.0...  >> '))
# number = float(input('Введите число для округления в формате x.x...>>  '))
#
# dig_after = abs(str(d).find('.') - len(str(d)))
# print(str(number)[:-dig_after])

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# number = int(input('Введите число >>  '))
# deliteli = []
#
# for i in range(1, number // 2 + 1):
#     if number % i == 0:
#         deliteli.append(i)
#
# print(f'Делители числа {number}: {deliteli}')

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# numbers = input('Введите числа через пробел >> ').split()
#
# # Строчечной функцией
# print(f'Уникальные элементы последовательности: {set(numbers)}')
#
# # Циклом
# uniq_num = []
# for i in range(len(numbers)):
#     if numbers[i] not in uniq_num:
#         uniq_num.append(numbers[i])
#
# print(uniq_num)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random


def write_file(st):
    with open('sem4.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 101)


def create_mn(k):
    lst = [rnd() for i in range(k + 1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))
