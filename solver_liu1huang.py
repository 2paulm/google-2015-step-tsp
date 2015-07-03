#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    #return math.trunc(math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2))
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)
    size=N
    matrixColumn = [[0] * N for i in range(N)]
    matrixRow = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            matrixRow[i][j] = matrixRow[j][i] = distance(cities[i], cities[j])
            matrixRow[i][i] = ""

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            else:
                dist[i][j] = ""

    #print matrixRow
    while size!=1:
        #print size
        size=size-1
        #print "here"
        #print matrixRow
        #print matrixColumn
        #print "done"
        for i in range(N):
            # get row minimization
            row_min = dist[i][j]
            for j in range(N):
                if dist[i][j] < row_min:
                    row_min = dist[i][j]


            if row_min != 0 and row_min != "":

                for j in range(N):
                    if j!=i and dist[i][j] != "":
                        # delta to minimization
                        dist[i][j] = dist[i][j] - row_min

        '''for i in range(N):
            for j in range(N):
                dist[j][i]=dist[i][j]'''

        for j in range(N):
            # get column minimization
            col_min = dist[i][j]
            for i in range(N):
                if dist[i][j] < col_min:
                    col_min = dist[i][j]

            if col_min != 0 and col_min!= "":
                for i in range(N):
                    if j!=i and dist[i][j] != "":
                        # delta to minimization
                        dist[i][j] = dist[i][j] - col_min

        '''for i in range(N):
            for j in range(N):
                matrixRow[j][i]=matrixColumn[i][j]'''
        # calculate panelty's of all 0's


        Column = [[0] * N for i in range(N)]
        Row = [[0] * N for i in range(N)]
        Zero = 0
        root = []
        for i in range(N):
            for j in range(N):
                if dist[i][j]==0:
                    for k in range(N):
                        if k != j :
                            Row[i][k] = dist[i][k]
                        else:
                            Row[i][k] = ""
                    for s in range(N):
                        if s !=i:
                            Column[j][s] = dist[s][j]
                        else:
                            Column[j][s] = ""

                    minColunm=min(Column[j])
                    minRow=min(Row[i])
                    if minColunm != "" and minRow != "":
                        countZero=minColunm+minRow
                        if countZero > Zero:
                            Zero = countZero
                            start = i
                            to = j
                            print Zero
        for q in range(N):
            dist[start][q] = ""
            dist[q][to] = ""
            #matrixRow[to][start]=""

        root.append([start,to])




    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
