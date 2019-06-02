########################################
# Subspace Skyline Algorithm
# @ Wenhui Yu, @ Huidi Zhang
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

import math
import time
from Library import read_data
from Library import order_points

def MSL2(G_size, Dimension, filename, N):
    [point_list, raw_list] = read_data(filename, N)
    time.clock()
    time0 = time.clock()
    order = order_points(raw_list, 0)
    time1 = time.clock()

    # initialize the first point to each layer
    point_list[order[0]].layer = 1
    layer = [[point_list[order[0]]]]
    sub_skyline = [[point_list[order[0]]]]

    # construct each layer
    Number = len(point_list)
    for i in range(1, Number):
        cur_p = point_list[order[i]]
        x1 = len(layer)
        x2 = 0
        layer_record = 0
        for skyline_point in sub_skyline[x1-1]:
            dominate = 1
            for ii in range(1, Dimension):
                if cur_p.coordination[ii] < skyline_point.coordination[ii]:
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
                for skyline_point in sub_skyline[x-1]:  # k is the layer of the i-th dimension, *len(layer[j])-k-1* to iterate in a reverse order
                    dominate = 1
                    for ii in range(1, Dimension):
                        if cur_p.coordination[ii] < skyline_point.coordination[ii]:
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
            if cur_p.layer > len(sub_skyline):  # if need to construct a new layer, we dont need to make a judge
                layer.append([cur_p])
                sub_skyline.append([cur_p])
            else:
                layer[layer_record].append(cur_p)
                for skyline_point in sub_skyline[layer_record]:  # if we store the current points to an existing layer, we need to remove the points dominated by the current point
                    dominate = 1
                    for ii in range(1, Dimension):
                        if skyline_point.coordination[ii] < cur_p.coordination[ii]:
                            dominate = 0
                            break
                    if dominate:
                        sub_skyline[layer_record].remove(skyline_point)
                sub_skyline[layer_record].append(cur_p)
    time2 = time.clock()
    return (layer, time1 - time0, time2 - time1, time2 - time0, math.log10(time2 - time0 + 0.1 ** 10))

