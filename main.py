#Tic-Tac-Toe

import os
import random


flat = [' ']*9
combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
s = os.sys.platform


def prnt():
    print('', flat[0], '|', flat[1], '|', flat[2], ' ')
    print('--- --- ---')
    print('', flat[3], '|', flat[4], '|', flat[5], ' ')
    print('--- --- ---')
    print('', flat[6], '|', flat[7], '|', flat[8], ' ')

def a_turn():
    x = input()
    if not x.isdigit() or not 1<=int(x)<=9 or flat[int(x)-1] != ' ':
        print('\nТак ходить нельзя\n')
        a_turn()
    else:
        flat[int(x)-1] = 'x'


def b_turn():
    x = random.randint(1,9)
    if flat[x-1] != ' ':
        b_turn()
    else:
        flat[x-1] = 'O'

def check_win(sym):
    for i, j, k in combinations:
        if flat[i]==flat[j]==flat[k]==sym:
            return True
    return False

def end_g():
    if check_win("x"):
        clrscr()
        print('Поздравляем! Вы победили!')
    elif check_win("O"):
        clrscr()
        print('Сожалеем, вы проиграли.')
    elif ' ' not in flat:
        clrscr()
        print('Оу, это ничья!')
    else:
        game()

def clrscr():
    if s[0] == 'w':
        os.system('cls')
    else:
        os.system('clear')

def game():
    a_turn()
    if ' ' not in flat:
        end_g()
    else:
        clrscr()
        prnt()
        b_turn()
        clrscr()
        prnt()
        end_g()
prnt()
game()
