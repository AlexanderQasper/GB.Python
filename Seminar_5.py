# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# orig_text = 'марат карат забвение квартал абдоминальный абвер'
# text1 = orig_text.split()
#
# print(*filter(lambda x: 'абв' not in x, text1))

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# 2.1. Человек против человека
from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
#
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


# 2.2. Добавьте игру против бота
def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# 3. Tic- Tac
# import pygame as pg
# import sys
#
# def check_win(mas, sign):
#     zeroes = 0
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(sign) == 3:
#             return sign
#     for col in range(3):
#         if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
#             return sign
#     if mas[0][0] == sign and mas[1][1] == sign and mas[2][2]:
#         return sign
#     if mas[0][2] == sign and mas[1][1] == sign and mas[2][0]:
#         return sign
#     if zeroes == 0:
#         return 'Piece'
#     return False
#
#
# pg.init()
# sizeblock = 100
# margine = 15
# width = heigth = sizeblock * 3 + margine * 4
# size_window = (width, heigth)
# screen = pg.display.set_mode(size_window)
#
# pg.display.set_caption('Крестики-нолики!')
#
# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)
# white = (255, 255, 255)
# mas = [[0] * 3 for i in range(3)]
#
# query = 0  # какой игрок ходит
# game_over = False
#
# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit()
#         elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
#             x_mouse, y_mouse = pg.mouse.get_pos()
#             col = x_mouse // (sizeblock + margine)
#             row = y_mouse // (sizeblock + margine)
#             if mas[row][col] == 0:
#                 if query % 2 == 0:
#                     mas[row][col] = 'x'
#                 else:
#                     mas[row][col] = 'o'
#                 query += 1
#
#         elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
#             game_over = False
#             mas = [[0] * 3 for i in range(3)]
#             query = 0
#             screen.fill(black)
#
#     if not game_over:
#         for row in range(3):
#             for col in range(3):
#                 if mas[row][col] == 'x':
#                     color = red
#                 elif mas[row][col] == 'o':
#                     color = green
#                 else:
#                     color = white
#                 x = col * sizeblock + (col + 1) * margine
#                 y = row * sizeblock + (row + 1) * margine
#                 pg.draw.rect(screen, color, (x, y, sizeblock, sizeblock))
#                 if color == red:
#                     pg.draw.line(screen, white, (x + 7, y + 7), (x + sizeblock - 7, y + sizeblock - 7), 3)
#                     pg.draw.line(screen, white, (x + 7, y + sizeblock - 7), (x + sizeblock - 7, y + 7), 3)
#                 elif color == green:
#                     pg.draw.circle(screen, white, (x + sizeblock // 2, y + sizeblock // 2), (sizeblock // 2 - 7), 3)
#         if (query - 1) % 2 == 0:
#             game_over = check_win(mas, 'x')
#         else:
#             game_over = check_win(mas, 'o')
#
#         if game_over:
#             screen.fill(black)
#             font = pg.font.SysFont('stxingkai', 80)
#             text1 = font.render(game_over, True, white)
#             text_rect = text1.get_rect()
#             text_x = screen.get_width() / 2 - text_rect.width / 2
#             text_y = screen.get_height() / 2 - text_rect.height / 2
#             screen.blit(text1, [text_x, text_y])
#
#     pg.display.update()
