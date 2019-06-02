import numpy as np
import math

def perm(l):
    if (len(l) <= 1):
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i + 1] + x)
    return r

def distance_brute_force(G1, G2):
    k = len(G1)
    d = len(G1[0])
    D = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            dis = 0
            for kk in range(d):
                dis += math.pow(G1[i][kk] - G2[j][kk], 2)
            dis = math.sqrt(dis)
            D[i][j] = dis

    stratgy_rec = [0] * k
    index = []
    for i in range(k):
        index.append(i)
    index_perm_list = perm(index)
    true_dis = 1000000
    for index_perm in index_perm_list:
        sum_dis = 0
        stratgy = [0] * k
        for i in range(k):
            sum_dis += D[i][index_perm[i]]
            stratgy[index_perm[i]] = i
        if sum_dis < true_dis:
            true_dis = sum_dis
            stratgy_rec = stratgy
    return true_dis, stratgy_rec
