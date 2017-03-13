# This is my first try at a tic tac toe game with an ai
import random
from os import system
import time
board = []
corner = ['7', '9', '1', '3']
side = ['4', '8', '6', '2']
center = ['5']


def setup():
    global master_board
    master_board = [' ']*10


def get_randint():
    return random.randint(0, 3)


def make_copy(board):
    dupe = []
    for i in range(0, 10):
        dupe.append(board[i])
    return dupe


def get_letter():
    letter = input("What letter do you want to be? (X/O): ").upper()
    while not (letter == "X" or letter == "O"):
        letter = input("Either the letter 'x' or 'o': ").upper()
    return letter


def det_first_player():
    choice = get_letter()
    if choice == "X":
        ##system('cls')
        print("You go first!")
        time.sleep(1)
        get_player_move(choice)
    else:
        ##system('cls')
        print("Computer goes first!")
        time.sleep(1)
        get_comp_move("X")


def show_master_board():
    print('   |   |')
    print(' ' + master_board[7] + ' | ' + master_board[8] + ' | ' + master_board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + master_board[4] + ' | ' + master_board[5] + ' | ' + master_board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + master_board[1] + ' | ' + master_board[2] + ' | ' + master_board[3])
    print('   |   |')


def get_player_move(letter):
    show_master_board()
    valid = False
    while valid is not True:
        move = input("Where do want to move on? (1-9)")
        if move not in '1 2 3 4 5 6 7 8 9'.split():
            print('You can only move on squares 1 to 9')
        elif not is_space_free(master_board, move) is True:
            print('This square has already been filled')
        else:
            valid = True
    else:
        make_move(master_board, letter, int(move))
        check_player_win(letter)


def check_player_win(letter):
    if check_win(master_board, letter) is True:
        print("player wins")
    elif is_board_full() is True:
        print("player det tie")
    else:
        get_comp_move(letter)


def is_space_free(board, number):
    if board[int(number)] != " ":
        return False
    else:
        return True


def check_win(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))


def make_move(board, player, move):
    board.pop(int(move))
    board.insert(int(move), player)
    check_win(board, player)


def is_board_full():
    for i in range(0, 10):
        if is_space_free(master_board, i):
            return False
        else:
            return True


def get_comp_move(letter):
    global comp_letter
    if letter is "X":
        comp_letter = "O"
    else:
        comp_letter = "X"
    for i in range(0, 10):
        copy = make_copy(master_board)
        make_move(copy, comp_letter, i)
        if check_win(copy, comp_letter):
            make_move(master_board, comp_letter, i)
    else:
        for i in range(0, 10):
            copy = make_copy(master_board)
            make_move(copy, letter, i)
            if check_win(copy, letter):
                make_move(master_board, comp_letter, i)
                check_comp_win()
        else:
            for i in corner:
                if is_space_free(master_board, i) is True:
                    make_move(master_board, comp_letter, int(corner[get_randint()]))
                    check_comp_win()
            else:
                if is_space_free(master_board, center[0]) is True:
                    make_move(master_board, comp_letter, center[0])
                    check_comp_win()
                else:
                    for i in side:
                        if is_space_free(master_board, i) is True:
                            make_move(master_board, comp_letter, int(side[get_randint()]))
                            check_comp_win()
                    else:
                        check_comp_win()


def check_comp_win():
    if check_win(master_board, comp_letter) is True:
        print("Comp wins")
    elif is_board_full() is True:
        print("Comp det tie")
    else:
        if comp_letter is "X":
            get_player_move("O")
        else:
            get_player_move("X")


def main():
    setup()
    det_first_player()
main()
