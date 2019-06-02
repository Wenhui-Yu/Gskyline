# -*- coding: utf-8 -*-
import numpy as np
def greedy_with_cost(D, k):
    conf = []
    b = []
    for i in range(k):
        for j in range(k):
            b.append((D[i][j],(i,j)))
    b.sort(key=lambda x: x[0])
    #print b
    num = 0
    sum_dis = 0
    Row = [k] * k
    row = list(Row)
    column = list(Row)
    for (dis,(x, y)) in b:
        if row[x] == k and column[y] == k:
            sum_dis += dis
            num += 1
            row[x] -= 1
            column[y] -= 1
        else:
            conf.append((dis,(x, y)))
        if num == k:
            break
    #print conf

    dis_reco = sum_dis
    while len(conf) > 0:
        ##初始化flag
        row = list(Row)
        column = list(Row)
        (dis, (x, y)) = conf[0]
        sum_dis = dis
        num = 1
        conf.remove((dis, (x, y)))
        row[x] -= 1
        column[y] -= 1
        for (dis, (x, y)) in b:
            if row[x] == k and column[y] == k:
                sum_dis += dis
                num += 1
                row[x] -= 1
                column[y] -= 1
                if (dis, (x, y)) in conf:
                    conf.remove((dis, (x, y)))
            if num == k:
                while (True):
                    if (len(conf) > 0 and conf[-1][0] > dis):
                        conf.pop()
                    else:
                        break
                break

        if sum_dis < dis_reco:
            dis_reco = sum_dis
    return dis_reco

