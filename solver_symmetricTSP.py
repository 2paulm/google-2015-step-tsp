#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input

# calculate min distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities):
    N = len(cities)

    # create original matrix with difference betwwen cities
    #A = numpy.zeros((N, N))
    A = [[None]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i][j] = ""
            else:
                A[i][j] = distance(cities[i], cities[j])

    # row minimization
    for i in range(N):
        min_row_value = A[i][1]
        for j in range(N):
            if A[i][j] < min_row_value:
                min_row_value = A[i][j]
            else:
                pass
        for j in range(N):
            if i != j:
                A[i][j] = abs(A[i][j] - min_row_value)

    # col minimizatoin
    for j in range(N):
        min_col_value = A[1][j]
        for i in range(N):
            if A[i][j] < min_col_value:
                min_col_value = A[i][j]
            else:
                pass
        for i in range(N):
            if i != j:
                A[i][j] = abs(A[i][j] - min_row_value)

    # calculate panelty's of all 0's
    while A is not None:
        for i in range(N):
            for j in range(N):
                penalty = 0
                max_penalty = 0
                tem_root = []
                root = []
                if i != j:
                    if A[i][j] == 0:
                        min_row = 0
                        min_col = 0
                        for s in range(N):
                            if A[s][j] < min_col:
                                A[s][j] = min_col
                            else:
                                pass
                        for t in range(N):
                            if A[i][t] < min_row:
                                A[i][t] = min_row
                            else:
                                pass
                        penalty = min_row + mincol
                        if penalty > max_penalty:
                            max_penalty = penalty
                            tem_root.append([i, j])
        root.append(tem_root[-1])
        A.row_del(tem_root[-1][0])
        A.cow_del(tem_root[-1][1])
        N -= 1
        for i in range(N):
            for j in range(N):
                if i != j:
                    if A[i][j] != 0:
                        A[i][j] = 1
                    else:
                        pass


    # links between cities
    start_city = root[0][0]
    solution.append(start_city)
    for pairs in root:
        solution.append(pairs[1])
    solution.remove(solution[-1])
    return solution

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
