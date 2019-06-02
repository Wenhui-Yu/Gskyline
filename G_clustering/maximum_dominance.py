########################################
# Fast UWise algorithm
# @ Wenhui Yu,
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

import numpy as np
import time

def maximum_dominance(g_skyline, k, filename, DSG, N):
    time1 = time.clock()
    G_size = len(g_skyline[0])
    Dimension = len(g_skyline[0][0].coordination)
    f = open(filename, 'r')
    lines = f.readlines()
    point_list = []
    #N =  len(lines)
    for i in range(0, N):
        line = lines[i]
        point = []
        for coord in line.split():
            point.append(float(coord))
        point_list.append(point)

    '''for layer in range(1, G_size + 1):
        for point in DSG.layer_dict[layer]:
            point_list.remove(point.coordination)
    #print 'point number', len(point_list)'''

    for group in g_skyline:
        for g_point in group:
            if not g_point.dominance_num:
                g_point.dominance = np.array([0] * N)
                for i in range(len(point_list)):
                    dominate = 1
                    for j in range(Dimension):
                        if point_list[i][j] < g_point.coordination[j]:
                            dominate = 0
                            break
                    if dominate:
                        g_point.dominance_num += 1
                        g_point.dominance[i] = 1

    cand_repre = []
    for i in range(k):
        dom_vec = np.array([0] * N)
        for j in range(G_size):
            dom_vec = dom_vec | g_skyline[i][j].dominance
        score = dom_vec.sum()
        cand_repre.append((score, g_skyline[i]))
    cand_repre.sort(key=lambda x: x[0])
    thre = cand_repre[0][0]
    for i in range(k + 1, len(g_skyline)):
        max_score = 0
        for point in g_skyline[i]:
            max_score += point.dominance_num
        if max_score > thre:
            dom_vec = np.array([0] * N)
            for point in g_skyline[i]:
                dom_vec = dom_vec | point.dominance
            score = dom_vec.sum()
            if score > thre:
                cand_repre[0] = (score, g_skyline[i])
        cand_repre.sort(key=lambda x: x[0])
        #print cand_repre
        thre = cand_repre[0][0]

    repre_skyline = []
    for group in cand_repre:
        repre_skyline.append(group[1])
    time2 = time.clock()
    return (repre_skyline, time2 - time1)
