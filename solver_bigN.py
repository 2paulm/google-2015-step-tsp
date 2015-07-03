#!/usr/bin/env python3

import sys
import math
from solver_mmpy import get_sol, distance
from common import print_solution, read_input
from cluster import KMeansClustering

>>> cl = KMeansClustering([(1,1), (2,1), (5,3), ...])
>>> clusters = cl.getclusters(2)


        group_num = (point_size/20) + 1
        reduced_size = point_size/group_num
        j = 0
        i = reduced_size
        if (point_size % 2) == 0:
            while i < point_size:
                get_sol(point_table[j, i], reduced_size)
                j += i
                i += i
        else:#(point_size % 2) == 1
            while i < point_size:
                if point_size % i != reduced_size:
                    get_sol(point_table[j, i], reduced_size)
                    j += i
                    i += i
                else:
                    #last one
                    get_sol(point_table[i, point_size], reduced_size+1)
