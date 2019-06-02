########################################
# MSL algorithm
# @ Wenhui Yu, @ Huidi Zhang
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

import math
import time
from Library import read_data
from Library import order_points

def MSL(G_size, Dimension, filename, N):
    [point_list, raw_list] = read_data(filename, N)
    time.clock()
    time0 = time.clock()
    order = order_points(raw_list, 1)
    time1 = time.clock()

    layer = []
    for i in range(G_size):
        layer.append([])
    sub_skyline = [] # to save the subspace skyline

    # initialize the first point to each layer
    for i in range(0, Dimension):
        point_list[order[i][0]].times = 1
        point_list[order[i][0]].layer = 1
        layer[0].append(point_list[order[i][0]])
        sub_skyline_row = []
        sub_skyline_column = []
        sub_skyline_row.append(point_list[order[i][0]])
        sub_skyline_column.append(sub_skyline_row)
        sub_skyline.append(sub_skyline_column)

    # construct each layer
    Number = len(point_list)
    for i in range(1, Number):
        for j in range(0, Dimension):
            _if_finished = 0
            point_list[order[j][i]].times += 1
            cur_p = point_list[order[j][i]]
            if cur_p.times == Dimension and cur_p.layer == G_size:
                _if_finished = 1
                break

            if cur_p.layer != 0:
                if cur_p.layer > len(sub_skyline[j]):
                    sub_skyline_row = []
                    sub_skyline_row.append(cur_p)
                    sub_skyline[j].append(sub_skyline_row)
                else:
                    for skyline_point in sub_skyline[j][cur_p.layer-1]:
                        dominate = 1
                        for ii in range(0, Dimension):
                            if ii != j and skyline_point.coordination[ii] < cur_p.coordination[ii]:
                                dominate = 0
                                break
                        if dominate:
                            sub_skyline[j][cur_p.layer-1].remove(skyline_point)
                    sub_skyline[j][cur_p.layer - 1].append(cur_p) # save in subspace skyline, and remove the point it dominates

            if cur_p.layer == 0:
                x1 = len(sub_skyline[j])
                x2 = 0

                for skyline_point in sub_skyline[j][x1-1]:  # binary searching
                    dominate = 1
                    layer_record = 0
                    for ii in range(0, Dimension):
                        if ii != j and cur_p.coordination[ii] < skyline_point.coordination[ii]:
                            dominate = 0
                            break
                    if dominate:
                        break
                if dominate:
                    layer_record = x1
                else:
                    while x1 - x2 > 1:
                        # x = (x1 + x2) / 2
                        x = (x1 + x2 + 1) / 2
                        for skyline_point in sub_skyline[j][x-1]:  # k is the layer of the i-th dimension, *len(layer[j])-k-1* to iterate in a reverse order
                            dominate = 1
                            layer_record = 0
                            for ii in range(0, Dimension):
                                if ii != j and cur_p.coordination[ii] < skyline_point.coordination[ii]:
                                    dominate = 0
                                    break
                            if dominate:
                                break
                        if dominate:
                            x2 = x
                        else:
                            x1 = x
                    layer_record = x2

                if layer_record < G_size:
                    cur_p.layer = layer_record + 1
                    layer[layer_record].append(cur_p)
                    if cur_p.layer > len(sub_skyline[j]):  # if need to construct a new layer, we dont need to make a judge
                        sub_skyline_row = []
                        sub_skyline_row.append(cur_p)
                        sub_skyline[j].append(sub_skyline_row)
                    else:
                        for skyline_point in sub_skyline[j][cur_p.layer-1]:  # if we store the current points to an existing layer, we need to remove the points dominated by the current point
                            dominate = 1
                            for ii in range(0, Dimension):
                                if ii != j and skyline_point.coordination[ii] < cur_p.coordination[ii]:
                                    dominate = 0
                                    break
                            if dominate:
                                sub_skyline[j][cur_p.layer-1].remove(skyline_point)
                        sub_skyline[j][cur_p.layer - 1].append(cur_p)
        if _if_finished:
            break
    time2 = time.clock()
    return (layer, time1 - time0, time2 - time1, time2 - time0, math.log10(time2 - time0 + 0.1 ** 10))

