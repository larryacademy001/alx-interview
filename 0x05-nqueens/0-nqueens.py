#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard. Write
a program that solves the N queens problem. """

from sys import argv


def is_NQueen(cell: list) -> bool:
    """ False if not N Queen, True if N Queen """
    row_num = len(cell) - 1
    dif = 0
    for index in range(0, row_num):
        dif = cell[index] - cell[row_num]
        if dif < 0:
            dif *= -1
        if dif == 0 or dif == row_num - index:
            return False
    return True


def solve_NQueens(dimension: int, row: int, cell: list, output: list):
    """ Return result of N Queens recursively """
    if row == dimension:
        print(output)
    else:
        for column in range(0, dimension):
            cell.append(column)
            output.append([row, column])
            if (is_NQueen(cell)):
                solve_NQueens(dimension, row + 1, cell, output)
            cell.pop()
            output.pop()


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    N = int(argv[1])
except BaseException:
    print('N must be a number')
    exit(1)
if N < 4:
    print('N must be at least 4')
    exit(1)
else:
    output = []
    cell = 0
    solve_NQueens(int(N), cell, [], output)
