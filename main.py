#Tic-Tac-Toe

import os
import random


flat = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
s = os.sys.platform


def prnt():
    print('', flat[0], '|', flat[1], '|', flat[2], ' ')
    print('--- --- ---')
    print('', flat[3], '|', flat[4], '|', flat[5], ' ')
    print('--- --- ---')
    print('', flat[6], '|', flat[7], '|', flat[8], ' ')

def a_turn():
    x = int(input())
    if flat[x-1] != ' ':
        print('')
        print('Эта клетка занята!')
        print('')
        a_turn()
    else:
        if x == 1:
            flat[x-1] = 'x'
        else:
            print('Такой ячейки не существует')

def b_turn():
    x = random.randint(1,9)
    if flat[x-1] != ' ':
        b_turn()
    else:
        if x == 1:
            flat[x-1] = 'O'
def end_g():
    if flat[0] == flat[1] == flat[2] == 'X' or flat[3] == flat[4] == flat[5] == 'X' or flat[6] == flat[7] == flat[8] == 'X' or flat[0] == flat[3] == flat[6] == 'X' or flat[1] == flat[4] == flat[7] == 'X' or flat[2] == flat[5] == flat[8] == 'X' or flat[0] == flat[4] == flat[8] == 'X' or flat[2] == flat[4] == flat[6] == 'X':
        clrscr()
        print('Поздравляем! Вы победили!')
        return 0
    elif flat[0] == flat[1] == flat[2] == 'O' or flat[3] == flat[4] == flat[5] == 'O' or flat[6] == flat[7] == flat[8] == 'O' or flat[0] == flat[3] == flat[6] == 'O' or flat[1] == flat[4] == flat[7] == 'O' or flat[2] == flat[5] == flat[8] == 'O' or flat[0] == flat[4] == flat[8] == 'O' or flat[2] == flat[4] == flat[6] == 'O':
        clrscr()
        print('Сожалеем, вы проиграли.')
        return 0
    elif flat[0] != ' ' and flat[1] != ' ' and flat[2] != ' ' and flat[3] != ' ' and flat[4] != ' ' and flat[5] != ' ' and flat[6] != ' ' and flat[7] != ' ' and flat[8] != ' ':
        clrscr()
        print('Оу, это ничья!')
        return 0
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
