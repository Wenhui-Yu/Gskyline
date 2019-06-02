########################################
# Fast UWise algorithm
# @ Wenhui Yu,
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

import numpy as np
import math

def distance(G1, G2):
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

    b = []
    for i in range(k):
        for j in range(k):
            b.append((D[i][j],(i,j)))
    b.sort(key=lambda x: x[0])
    conf = list(b)

    stratgy = [0] * k
    stratgy_rec = [0] * k
    Row = [k] * k
    dis_reco = 100000
    while len(conf) > 0:
        # initialize flag
        row = list(Row)
        column = list(Row)
        (dis, (x, y)) = conf[0]
        stratgy[y] = x
        sum_dis = dis
        num = 1
        conf.remove((dis, (x, y)))
        row[x] -= 1
        column[y] -= 1
        for (dis, (x, y)) in b:
            if row[x] == k and column[y] == k:
                sum_dis += dis
                stratgy[y] = x
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
            stratgy_rec = stratgy
    return dis_reco, stratgy_rec

