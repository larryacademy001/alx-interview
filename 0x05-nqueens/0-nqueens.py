#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard. Write
a program that solves the N queens problem. """

import sys


def backtrack(cur_row, size, cols, pos, neg, board):
    """
    backtrack function to find solution
    """
    if cur_row == size:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for s in range(size):
        if s in cols or (cur_row + s) in pos or (cur_row - s) in neg:
            continue

        cols.add(s)
        pos.add(cur_row + s)
        neg.add(cur_row - s)
        board[cur_row][s] = 1

        backtrack(cur_row+1, size, cols, pos, neg, board)

        cols.remove(s)
        pos.remove(cur_row + s)
        neg.remove(cur_row - s)
        board[cur_row][s] = 0


def nqueens(num_queens):
    """
    Solution to nqueens problem
    Args:
        num_queens (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * num_queens for i in range(num_queens)]

    backtrack(0, num_queens, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
