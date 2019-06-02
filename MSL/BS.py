########################################
# BS algorithm
# @ Wenhui Yu, @ Huidi Zhang
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################
import math
import time
from Library import read_data
from Library import order_points

def BS(G_size, Dimension, filename, N):
    [point_list, raw_list] = read_data(filename, N)
    time.clock()
    time0 = time.clock()
    order = order_points(raw_list, 0)
    time1 = time.clock()

    layer = []
    point_list[order[0]].layer = 1
    layer_row = []
    layer_row.append(point_list[order[0]])
    layer.append(layer_row)

    Number = len(point_list)
    for i in range(1, Number):
        cur_p = point_list[order[i]]
        x1 = len(layer)
        x2 = 0
        for pro_p in layer[x1 - 1]:
            dominate = 1
            layer_record = 0
            for ii in range(0, Dimension):
                if cur_p.coordination[ii] < pro_p.coordination[ii]:
                    dominate = 0
                    break
            if dominate:
                break
        if dominate:
            layer_record = x1
        else:
            while x1 - x2 > 1:
                x = (x1 + x2 + 1) / 2
                for pro_p in layer[x - 1]:
                    dominate = 1
                    layer_record = 0
                    for ii in range(0, Dimension):
                        if cur_p.coordination[ii] < pro_p.coordination[ii]:
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
            if cur_p.layer > len(layer):
                layer_row = []
                layer_row.append(cur_p)
                layer.append(layer_row)
            else:
                layer[cur_p.layer - 1].append(cur_p)
    time2 = time.clock()
    return (layer, time1 - time0, time2 - time1, time2 - time0, math.log10(time2 - time0 + 0.1 ** 10))