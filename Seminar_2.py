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

# 4. Орёл и решка

stroka = input().split('О')

print(max(map(len, stroka)))
