# 1. Вычислить число c заданной точностью d

# d = float(input('Введите степень точности в формате 0.0...  >> '))
# number = float(input('Введите число для округления в формате x.x...>>  '))
#
# dig_after = abs(str(d).find('.') - len(str(d)))
# print(str(number)[:-dig_after])

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число >>  '))
deliteli = []

for i in range(1, number // 2 + 1):
    if number % i == 0:
        deliteli.append(i)

print(f'Делители числа {number}: {deliteli}')
