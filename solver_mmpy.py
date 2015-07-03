#!/usr/bin/env python3

import sys
import math
from common import print_solution, read_input
#from Tkinter import *
from cluster import KMeansClustering


def distance(ps):
    size = len(ps)
    table = [[0] * size for _ in xrange(size)]
    for i in xrange(size):
        for j in xrange(size):
            if i != j:
                dx = ps[i][0] - ps[j][0]
                dy = ps[i][1] - ps[j][1]
                table[i][j] = math.sqrt(dx * dx + dy * dy)
    return table

def memoize(f):
    table = {}
    def func(*args):
        if not args in table:
            table[args] = f(*args)
        return table[args]
    return func

def tsp(p, v):
    if (1 << point_size) - 1 == v:
        return distance_table[p][0]
    else:
        return min([distance_table[p][x] + tsp(x, v | (1 << x)) \
                    for x in xrange(point_size) if not (v & (1 << x))])

tsp = memoize(tsp)

def tsp_dp(size):
    size1 = size - 1
    table = [None] * (1 << size1)
    table[(1 << size1) - 1] = [distance_table[i][0] for i in xrange(1, size)]
    for v in xrange((1 << size1) - 2, 0, -1):
        tmp = [1e300] * size1
        for i in xrange(size1):
            if (1 << i) & v:
                tmp[i] = min([distance_table[i+1][j+1] + table[v | (1 << j)][j] \
                             for j in xrange(size1) if not (1 << j) & v])
        table[v] = tmp
    return min([distance_table[i+1][0] + table[1 << i][i] for i in xrange(size1)])


def min0(ary):
    v = (1e300, None)
    for x in ary:
        if v[0] > x[0]: v = x
    return v

def tsp_dp1(size):
    size1 = size - 1
    table = [None] * (1 << size1)
    table[(1 << size1) - 1] = [(distance_table[i][0], 0) for i in xrange(1, size)]
    for v in xrange((1 << size1) - 2, 0, -1):
        tmp = [1e300] * size1
        for i in xrange(size1):
            if (1 << i) & v:
                tmp[i] = min0([(distance_table[i+1][j+1] + table[v | (1 << j)][j][0], j) \
                               for j in xrange(size1) if not (1 << j) & v])
        table[v] = tmp
    s = min0([(distance_table[i+1][0] + table[1 << i][i][0], i) for i in xrange(size1)])
    return s[0], get_min_path(table, size, s[1])

def get_min_path(table, size, p):
    path = [0, p + 1]
    v = 1 << p
    while len(path) < size:
        _, q = table[v][p]
        path.append(q + 1)
        v |= (1 << q)
        p = q
    return path


def get_sol(size):
    min_len, min_path = tsp_dp1(size)
    #min_len = tsp_dp(point_size)
    #min_path = []
    print min_len
    print_solution(min_path)

'''def divide_group(point_table, point_size):
    if point_size <= 20:
        distance_table = distance(point_table)
        get_sol(point_size)
    else:
        cl = KMeansClustering(point_table)
        group_num = (point_size/20) + 1
        clusters = cl.getclusters(group_num)
        for groups in clusters:
            #point_table = groups
            distance_table = distance(groups)
            get_sol(len(groups))'''

def cal_min_groups(list1, list2):
    i = 0
    j = 0
    min_dis = math.sqrt((list1[i][0] - list2[j][0]) ** 2 + (list1[i][1] - list2[j][1]) ** 2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            dis = math.sqrt((list1[i][0] - list2[j][0]) ** 2 + (list1[i][1] - list2[j][1]) ** 2)
            if dis < min_dis:
                min_dis = dis
    return min_dis



if __name__ == '__main__':
    point_table = read_input(sys.argv[1])
    point_size = len(point_table)
    if point_size <= 20:
        distance_table = distance(point_table)
        get_sol(point_size)
    else:
        cl = KMeansClustering(point_table)
        group_num = (point_size/20) + 1
        clusters = cl.getclusters(group_num)
        group_lists = []
        for groups in clusters:
            distance_table = distance(groups)
            get_sol(len(groups))
            group_lists.append(groups)
        g = 0
        group_dis = 0.0
        min_group_dis_list = []
        s = g+1
        for g in range(len(group_lists)-1):
            while s < len(group_lists)-1:
                group_dis += cal_min_groups(group_lists[g], group_lists[s])
                s += 1
            min_group_dis_list.append(group_dis)
            min_group_dis = min(min_group_dis_list)
        print min_group_dis
    #divide_group(point_table, point_size)
