########################################
# Multiple Dimensional Searching Algorithm
# @ Wenhui Yu, @ Huidi Zhang
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

import math
import time
from Library import read_data
from Library import order_points

def MSL1(G_size, Dimension, filename, N):
    [point_list, raw_list] = read_data(filename, N)
    time.clock()
    time0 = time.clock()
    order = order_points(raw_list, 1)
    time1 = time.clock()

    # initialize the first point to each layer
    Layer = []
    for i in range(G_size):
        Layer.append([])
    layer = []
    for i in range(0, Dimension):
        point_list[order[i][0]].times = 1
        point_list[order[i][0]].layer = 1
        Layer[0].append(point_list[order[i][0]])
        layer_row = []
        layer_column = []
        layer_row.append(point_list[order[i][0]])
        layer_column.append(layer_row)
        layer.append(layer_column)

    # construct each layer
    Number = len(point_list)
    for i in range(1, Number):
        for j in range(0, Dimension):
            _if_finished = 0
            point_list[order[j][i]].times += 1
            cur_p = point_list[order[j][i]]
            if cur_p.times == Dimension and cur_p.layer == G_size:
                if cur_p.layer > len(layer[j]):
                    layer_row = []
                    layer_row.append(cur_p)
                    layer[j].append(layer_row)
                else:
                    layer[j][cur_p.layer - 1].append(cur_p)
                _if_finished = 1
                break

            if cur_p.layer != 0:
                if cur_p.layer > len(layer[j]):
                    layer_row = []
                    layer_row.append(cur_p)
                    layer[j].append(layer_row)
                else:
                    layer[j][cur_p.layer - 1].append(cur_p)

            if cur_p.layer == 0:
                for k in range(0, len(layer[j])):
                    flag = 0
                    for pro_p in layer[j][len(layer[j])-k-1]:
                        dominate = 1
                        layer_record = 0
                        for ii in range(0, Dimension):
                            if cur_p.coordination[ii] < pro_p.coordination[ii]:
                                dominate = 0
                                break
                        if dominate:
                            layer_record = pro_p.layer
                            flag = 1
                            break
                    if flag:
                        break
                if layer_record < G_size:
                    cur_p.layer = layer_record + 1
                    Layer[layer_record].append(cur_p)
                    if cur_p.layer > len(layer[j]):
                        layer_row = []
                        layer_row.append(cur_p)
                        layer[j].append(layer_row)
                    else:
                        layer[j][cur_p.layer - 1].append(cur_p)
        if _if_finished:
            break

    com_layer = []
    for i in range(0, G_size):
        sin_layer = []
        for k in range(0, Dimension):
            sin_layer += layer[k][i]
        com_layer.append(list(set(sin_layer)))
    time2 = time.clock()
    return (Layer, time1 - time0, time2 - time1, time2 - time0, math.log10(time2 - time0 + 0.1 ** 10))
