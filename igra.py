import numpy as np
import random

pole_1 = [[f'{a}{b}' for b in range(0, 10)] for a in range(0, 10)]  # 100 ячеек


def print_pole(pole):  # вывод поля 10х10
    for pp in pole:  # [10 11 12 13 . . .]
        print('|', end=' ')
        for p in pp:  # [10]
            print('%3s' % p, end=' | ')
        print()

def hod_konyom(pole, player='x', place=None):  # лист[[11],[22]], метка(x,о), место в листе(11,22)
    pole[int(place[0])][int(place[1])] = player

def check_luz(pole, player):  # проверка на проигрыш
    for pp in pole:  # проверка по горизонту
        for p in range(int(len(pp) / 2)):
            if set(pp[p:p + 5]) == set(player):
                return player

def check_all(pole,player):
    trans_pole = np.transpose(pole)  # переворачиваем поле
    d_pole = dio_pole(pole)  # создание диагонального поля 00 - 05
    dt_pole = dio_pole(trans_pole)  # создание диагонального поля 00 - 50
    dr_pole = dior_pole(pole)  # создание рд поля 09-04
    dtr_pole = dior_pole(trans_pole)  # создание врд поля 90-40
    list_pol = [pole, trans_pole, d_pole, dt_pole, dr_pole, dtr_pole] # список полей
    if cycle_check(list_pol, player)==player: # проверяем по списку все поля
        return player

def cycle_check(list_pol, player):
    for pole in list_pol:
        if check_luz(pole,player)==player:
            return player


def dio_pole(pole):  # создаем поле диагонали
    dia_pole, dd_pole = [], []
    for ii in range(6):
        for u in range(10 - ii):
            dia_pole.append(pole[u + ii][u])  # 00-55
    for uu in range(10, 4, -1):
        dd_pole.extend([dia_pole[:uu]])
        dia_pole = dia_pole[uu:]
    return dd_pole

def dior_pole(pole):  # создаем поле реверса диагонали
    dia_pole, dd_pole = [], []
    for ii in range(6):
        for u in range(10 - ii):
            dia_pole.append(pole[u][-(u+1+ii)])  # 09-04
    for uu in range(10, 4, -1):
        dd_pole.extend([dia_pole[:uu]])
        dia_pole = dia_pole[uu:]
    return dd_pole

def check_pos(pole, pos=None): # проверка на занятость позиции
    if pole[int(pos[0])][int(pos[1])] in ['x', 'o']:
        return 'wrong place'
    else:
        return 'ok'

def check_hod(pos, pm): # проверка можно ли ходить в ячейку
    if check_pos(pole_1, pos)== 'ok':
        hod_konyom(pole_1, pm, pos)
    elif check_pos(pole_1, pos) == 'wrong place':
        if pm=='x':
            return check_hod(input("Подумай еще 00-99 :"),'x') # выбор для игрока
        elif pm=='o':
            return check_hod(f'{random.randint(00, 99):02d}','o') # выбор для компа

print('Игра 5 в ряд - поражение')
game = 1

while 0<game:
    print_pole(pole_1)
    check_hod(input("Выбор позиции 00-99 :"),'x')
    check_hod(f'{random.randint(00, 99):02d}','o')

    if check_all(pole_1, 'x')=='x':
        print('end game\nигрок проиграл')
        game-=1
    elif check_all(pole_1, 'o')=='o':
        print('end game\nкомп проиграл')
        game-=1
