########################################
# BL algorithm
# @ Wenhui Yu, @ Huidi Zhang
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################
import math
import time
from Library import read_data
from Library import order_points

def BL(G_size, Dimension, filename, N):
    [point_list, raw_list] = read_data(filename, N)
    time.clock()
    time0 = time.clock()
    order = order_points(raw_list, 0)
    time1 = time.clock()

    # initialize the first point
    layer = []
    Number = len(point_list)
    for ii in range(1, G_size+1):
        for jj in range(0, Number):
            if point_list[order[jj]].layer == 0:
                point_list[order[jj]].layer = ii
                break

        layer_row = []
        layer_row.append(point_list[order[jj]])

        for i in range(jj+1, Number):
            '''if i%1000 == 0:
                print i'''
            if point_list[order[i]].layer == 0:
                cur_p = point_list[order[i]]
                cur_p.layer = ii

                for pro_p in layer_row:
                    dominate = 1
                    for ii in range(0, Dimension):
                        if cur_p.coordination[ii] < pro_p.coordination[ii]:
                            dominate = 0
                            break
                    if dominate:
                        cur_p.layer = 0
                        break
                if cur_p.layer != 0:
                    layer_row.append(cur_p)
        layer.append(layer_row)

    time2 = time.clock()
    return (layer, time1 - time0, time2 - time1, time2 - time0, math.log10(time2 - time0 + 0.1 ** 10))

