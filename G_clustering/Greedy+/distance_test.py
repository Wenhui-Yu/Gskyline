# -*- coding: utf-8 -*-
import numpy as np
from numpy import *
import time
import math
import itertools #for quick combinations and permutations
import time
from Hungarian import Hungarian
from pruning_tree import pruning_tree
from greedy_with_cost import greedy_with_cost
from greedy import greedy
from greedy_plus import greedy_plus
from true_distance import true_distance
#to calculate the distance of pair of points
def distance(p1, p2):
    dis = 0
    for i in range(d):
        dis += pow((p1[i] - p2[i]), 2)
    return math.sqrt(dis)

def distance_generate():
    P1 = []
    P2 = []
    for i in range(k):
        p = []
        for j in range(d):
            p.append(random.random())
        P1.append(p)
        p = []
        for j in range(d):
            p.append(random.random())
        P2.append(p)
    D = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            D[i][j] = distance(P1[i], P2[j])
    return D

k = 2
iter = 1000
d = 2
e = 0.000001

H = 0
G = 0
P = 0

tt = 0
th = 0
tg = 0
tp = 0
for i in range(iter):
    D = distance_generate()
    t0 = time.clock()
    t = true_distance(D, k)
    #t = Hungarian(D)
    t1 = time.clock()
    h = Hungarian(D)
    t2 = time.clock()
    g = greedy(D, k)
    t3 = time.clock()
    p = greedy_plus(D, k)
    #p = greedy_with_cost(D, k)
    t4 = time.clock()

    H += abs(h - t)
    G += abs(g - t)
    P += abs(p - t)

    tt += t1 - t0
    th += t2 - t1
    tg += t3 - t2
    tp += t4 - t3

print H/iter,'\t', G/iter,'\t', P/iter
print tt/iter*1000,'\t',th/iter*1000,'\t',tg/iter*1000,'\t',tp/iter*1000



