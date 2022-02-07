import numpy as np
import random

field_1 = [[f'{a}{b}' for b in range(0, 10)] for a in range(0, 10)]  # 100 ячеек

def print_field(field):  # вывод поля 10х10
    for pp in field:  # [10 11 12 13 . . .]
        print('|', end=' ')
        for p in pp:  # [10]
            if p == 'x':
                print('\x1b[1m\x1b[32m%3s\x1b[0m' % p, end=' | ')
            elif p == 'o':
                print('\033[1m\033[31m%3s\033[0m' % p, end=' | ')
            else:
                print('\033[2m%3s\033[0m' % p, end=' | ')
        print()

def set_turn(field, player, place=None):  # лист[[11],[22]], метка(x,о), место в листе(11,22)
    field[int(place[0])][int(place[1])] = player

def check_lose(field, player):  # проверка на проигрыш
    for cell in field:  # проверка по горизонту
        for i in range(int(len(cell) / 2)):
            if set(cell[i:i + 5]) == set(player):
                return player

def check_all(field, player):
    trans_field = np.transpose(field)  # переворачиваем поле
    d_field = dio_field(field)  # создание диагонального поля 00 - 05
    dt_field = dio_field(trans_field)  # создание диагонального поля 00 - 50
    dr_field = dior_field(field)  # создание рд поля 09-04
    dtr_field = dior_field(trans_field)  # создание врд поля 90-40
    list_field = [field, trans_field, d_field, dt_field, dr_field, dtr_field] # список полей
    if cycle_check(list_field, player)==player: # проверяем по списку все поля
        return player

def cycle_check(list_field, player):
    for field in list_field:
        if check_lose(field, player)==player:
            return player


def dio_field(field):  # создаем поле диагонали
    dia_field, dd_field = [], []
    for ii in range(6):
        for u in range(10 - ii):
            dia_field.append(field[u + ii][u])  # 00-55
    for uu in range(10, 4, -1):
        dd_field.extend([dia_field[:uu]])
        dia_field = dia_field[uu:]
    return dd_field

def dior_field(field):  # создаем поле реверса диагонали
    dia_field, dd_field = [], []
    for ii in range(6):
        for u in range(10 - ii):
            dia_field.append(field[u][-(u + 1 + ii)])  # 09-04
    for uu in range(10, 4, -1):
        dd_field.extend([dia_field[:uu]])
        dia_field = dia_field[uu:]
    return dd_field

def check_pos(field, pos=None): # проверка на занятость позиции
    if field[int(pos[0])][int(pos[1])] in ['x', 'o']:
        return 'wrong place'
    else:
        return 'ok'

def check_turn(pos, player_marker): # проверка можно ли ходить в ячейку
    if check_pos(field_1, pos)== 'ok':
        set_turn(field_1, player_marker, pos)
    elif check_pos(field_1, pos) == 'wrong place':
        if player_marker=='x':                                 # выбор для игрока
            return input_player('Try another position')
        elif player_marker=='o':
            return check_turn(f'{random.randint(00, 99):02d}', 'o') # выбор для компа

def input_player(text): # функция ввода игрока с встроенной проверкой
    x = input(f"{text} 00-99 :")
    try:
        check_turn(x, 'x')
    except:  # защита от ValueError: invalid literal for int() with base 10: 's'
        check_turn(f'{len(x):02d}', 'x')


print('Game five in a row - lost')
game = 1
print_field(field_1)

while 0<game:
    input_player('Position selection')
    check_turn(f'{random.randint(00, 99):02d}', 'o')
    print_field(field_1)
    if check_all(field_1, 'x')== 'x':
        print('end game\n\x1b[1m\x1b[32m(player lose)\x1b[0m')
        game-=1
    elif check_all(field_1, 'o')== 'o':
        print('end game\n\033[1m\033[31m(computer lose)\033[0m')
        game-=1
