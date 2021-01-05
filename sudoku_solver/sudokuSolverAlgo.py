# functions:
#               show board in good way
#               finding empty place at the board
#               check if number is valid
#               put on empty place number that can fit
#               solving sudoku place by place

import copy
from sudokuGenerator import *

# -------- Global board ----------------
# Board = [[]]

Board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

solvedBoard = copy.deepcopy(Board)
# Board = [
#         [7, 8, 0, 4, 0, 0, 1, 2, 0],
#         [6, 0, 0, 0, 7, 5, 0, 0, 9],
#         [0, 0, 0, 6, 0, 1, 0, 7, 8],
#         [0, 0, 7, 0, 4, 0, 2, 6, 0],
#         [0, 0, 1, 0, 5, 0, 9, 3, 0],
#         [9, 0, 4, 0, 6, 0, 0, 0, 5],
#         [0, 7, 0, 3, 0, 0, 0, 1, 2],
#         [1, 2, 0, 0, 0, 7, 4, 0, 0],
#         [0, 4, 9, 2, 0, 6, 0, 0, 7]
#     ]
# def printBoard(board):
#     for i in range(len(board)):
#         if i % 3 == 0 and i != 0:
#             print("- - - - - - - - - - - -")
#         for j in range(len(board[0])):
#             if j % 3 == 0 and j != 0:
#                 print(" | ", end="")
#             if j == 8:  # end of the row
#                 print(board[i][j])
#             else:
#                 print(str(board[i][j]) + " ", end="")
#
#
# def findEmpty(board):
#     for y in range(len(board)):
#         for x in range(len(board[0])):
#             if board[y][x] == 0:
#                 return y, x  # y = row , x = column
#     # if we got here it mean that we finish the sudoku, so return none
#     return None


# def validCheck(board, number, coordinates):
#     # checking row
#     for x in range(len(board[0])):
#         if number == board[coordinates[0]][x] and coordinates[1] != x:  # coordinates[0]= row
#             return False
#
#     # checking column
#     for y in range(len(board)):
#         if number == board[y][coordinates[1]] and coordinates[0] != y:
#             return False
#
#     # checking the box
#     box_x = coordinates[1] // 3
#     box_y = coordinates[0] // 3
#
#     for y in range(box_y * 3, box_y * 3 + 3):
#         for x in range(box_x * 3, box_x * 3 + 3):
#             if number == board[y][x] and (y, x) != coordinates:
#                 return False
#
#     return True


def solve(board):
    # end condition:- getting to the end of the board - the function findEmpty return NONE
    find = findEmpty(board)
    if find is None:  # if find != False
        return True
    else:
        row, col = find
    for number in range(1, 10):
        if validCheck(board, number, (row, col)):
            board[row][col] = number
            # TODO: need to show it on the GUI

            if solve(board):
                return True

            board[row][col] = 0
            # TODO: delete the number in the GUI
    return False


def mainSolver(level):
    sudokuGenerate(Board, level)
    # solvedBoard = copy.deepcopy(Board)
    # print("Board")
    # printBoard(Board)
    solvedBoard = copy.deepcopy(Board)
    solve(solvedBoard)
    return solvedBoard
    # print("\n___________________________\n")
    # print("solvedBoard")
    # printBoard(solvedBoard)

#

# mainSolver(2)
# print("solveBoard")
# printBoard(solvedBoard)