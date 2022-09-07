# 1. Холодильники с антоном
# n = int(input())
# list1 = []
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)
#
# print(*list1)

# 2. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:  - Для N = 5: 1, -3, 9, -27, 81

# print([(-3)**i for i in range(int(input()))])

# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой

# a = 'pyt'
# b = 'pythonpythonpythonpythonpython'
# print(b.count(a))

# 4. Орёл и решка. ОРРОРОРООРРРО - 3, ООООООРРРОРОРРРРРРР - 7

# stroka = input().split('О')
# print(max(map(len, stroka)))

# 5. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# 1 var. OLD School!!!
# number = int(input())
# sum = 0
#
# while number > 0:
#     digit = number % 10
#     sum += digit
#     number //= 10
#
# print(sum)

# 2 var. В одну строчку! (не надо так...)

# print(*[sum(int(i) for i in input() if i.isnumeric())])

# 6. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# summa = 0
# for i in range(1, int(input()) + 1):
#     summa += ((1 + 1 / i)**i)
# print(summa)

# 7. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint

number = int(input())
pos1 = int(input(f'Введите первую позицию (не больше) {number} - '))
pos2 = int(input(f'Введите вторую позицию (не больше) {number} - '))

if pos1 <= number and pos2 <= number:
    with open("file.txt", "w") as f:
        numbers = []
        for i in range(number):
            numbers.append(randint(number * -1, number + 1))
            f.write(str(numbers[i]) + '\n')
    print(numbers)

    mulptiple_num = numbers[pos1 - 1] * numbers[pos2 - 1]
    print("Произведение: ", mulptiple_num)
    with open("file.txt", "a") as f:
        f.write(f'Произведение позиций массива = {str(mulptiple_num)}')

else:
    print('Ошибка!')
