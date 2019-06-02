########################################
# Fast UWise algorithm
# @ Wenhui Yu,
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

from distance import distance
import numpy as np
from xlrd import open_workbook
from xlutils.copy import copy

def repre_output(g_skyline, represent_skyline, flag):
    if flag == 1:
        k = len(represent_skyline)
        g_cen = []
        for i in range(k):
            g_cen.append([])
        for g in g_skyline:
            G = []
            for p in g:
                G.append(p.coordination)
            G = np.array(G)
            dis_rec = 1000000
            g_rec = -1
            for gc in range(len(represent_skyline)):
                Gc = []
                for p in represent_skyline[gc]:
                    Gc.append(p.coordination)
                Gc = np.array(Gc)
                [dis, u] = distance(G, Gc)
                if dis < dis_rec:
                    dis_rec = dis
                    g_rec = gc
            g_cen[g_rec].append(g)
        for gc in range(len(represent_skyline)):
            for p in represent_skyline[gc]:
                print p.id + 1, p.coordination,
            print '  ',
            for g in g_cen[gc]:
                for p in g:
                    print p.id + 1, p.coordination,
                print ' ',
            print
    if flag == 0:
        for group in represent_skyline:
            for point in group:
                print point.id, point.coordination, '\t',
            print
        print
    max_score = [33.400000, 15.600000, 12.300000, 3.000000, 3.500000]
    if flag == 2:
        for group in represent_skyline:
            for point in group:
                score = []
                for coor in range(len(point.coordination)):
                    score.append(max_score[coor] - point.coordination[coor])
                print point.id, score, '\t',
            print
        print
    return 0

def save_result(intro, F1, NDCG, path):
    rexcel = open_workbook(path)
    rows = rexcel.sheets()[0].nrows
    excel = copy(rexcel)
    table = excel.get_sheet(0)
    row = rows
    table.write(row, 0, intro)
    #table.write(row, 2, 'F1')
    for i in range(len(F1)):
        table.write(row, i + 3, F1[i])
    #table.write(row, len(F1) + 4, 'NDCG')
    for i in range(len(NDCG)):
        table.write(row, i + len(F1) + 5, NDCG[i])
    excel.save(path)