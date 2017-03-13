# This is my first try at a tic tac toe game with a 1v1 system
import random
from os import system
import time
board = []


def setup():
    global board
    board = [' ']*10


def get_letter():
    letter = input("What letter do you want to be? (X/O): ").upper()
    while not (letter == "X" or letter == "O"):
        letter = input("Either the letter 'x' or 'o': ").upper()
    return letter


def det_first_player():
    choice = get_letter()
    if choice == "X":
        global player1
        player1 = "X"
        system('cls')
        print("You go first!")
        time.sleep(1)
        get_player_move()
    else:
        global player2
        player2 = "O"
        system('cls')
        print("Computer goes first!")
        time.sleep(1)


def show_board():
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def get_player_move():
    show_board()
    valid = False
    while valid is not True:
        move = input("Where do want to move on? (1-9)")
        if move not in '1 2 3 4 5 6 7 8 9'.split():
            print('You can only move on squares 1 to 9')
        elif not is_space_free(move) is True:
            print('This square has already been filled')
        else:
            valid = True
    else:
        make_move("X", int(move))


def is_space_free(number):
    if board[int(number)] != " ":
        return False
    else:
        return True


def make_move(player, move):
    board.pop(move)
    board.insert(move, player)
    show_board()
    get_comp_move()

setup()


get_player_move()


def check_won(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))


def is_board_full():
    for i in range(0, 10):
        if is_space_free(i):
            return False
        else:
            return True
