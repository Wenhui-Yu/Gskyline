########################################
# PWise algorithm
# @ Wenhui Yu
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

import time
import math

def PWise(G_size, test):
    time.clock()
    time1 = time.clock()
    candidate_skyline = []
    g_skyline = []
    g_list = []
    group = []
    for item in test.layer_dict[1]:
        group.append(item)
        g_list.append(group)
        group = []

    list_p = 0
    while len(g_list[list_p]) < G_size:
        group = g_list[list_p]   #record the current group
        last_p = group[len(group)-1]  #record the last point in current group
        candidate_set = []
        if last_p.layer == 1:
            for point in range(last_p.layer_location+1, len(test.layer_dict[1])):
                candidate_set.append(test.layer_dict[1][point])
        for point in group:
            for child_id in point.child_id_set:
                if test.DSG_point_dict[child_id].layer-point.layer == 1 \
                        and (last_p.layer < test.DSG_point_dict[child_id].layer \
                        or (last_p.layer == test.DSG_point_dict[child_id].layer \
                        and last_p.layer_location < test.DSG_point_dict[child_id].layer_location)):
                    candidate_set.append(test.DSG_point_dict[child_id])

        g = []
        for i in candidate_set:
            g.append(i.id)
        g = list(set(g))
        candidate_set = []
        for i in g:
            candidate_set.append(test.DSG_point_dict[i])

        for point in candidate_set:
            f = []
            flag = 1
            parent_list = []
            if len(point.parent_id_set) > 0:
                parent_list = list(point.parent_id_set)
                for i in range(0, len(point.parent_id_set)):
                    f.append(0)
                    for j in group:
                        if j.id == parent_list[i]:
                            f[i] = 1
                for i in f:
                    flag = flag*i
            if flag:
                new_group = list(group)
                new_group.append(point)
                g_list.append(new_group)
                if len(new_group) == G_size:
                    candidate_skyline.append(new_group)
                new_group = list(group)
        list_p += 1
        if list_p == len(g_list):
            break
    time2 = time.clock()
    return (candidate_skyline, time2 - time1, math.log10(time2 - time1 + 0.1 ** 10))

