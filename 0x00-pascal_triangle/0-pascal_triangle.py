#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n <= 0
"""

def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    result = []
    if n <= 0:
        return result
    result = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(result[i - 1]) - 1):
            curr = result[i - 1]
            temp.append(result[i - 1][j] + result[i - 1][j + 1])
        temp.append(1)
        result.append(temp)
    return result
