########################################
# Fast PWise algorithm
# @ Wenhui Yu
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

import time
import math

def F_PWise(G_size, DSG):
    time.clock()
    time1 = time.clock()
    # generate combination
    candidate_list = []
    group = []
    g_skyline = []
    for point in DSG.layer_dict[1]:
        group.append(point)
        candidate_list.append(group)
        group = []
    list_point = 0
    while list_point < len(candidate_list):
        group = list(candidate_list[list_point])
        if len(group) < G_size - 1:
            for i in range(group[len(group)-1].layer_location+1, len(DSG.layer_dict[1])):
                group.append(DSG.layer_dict[1][i])
                candidate_list.append(group)
                group = list(candidate_list[list_point])
        list_point += 1

    # prune DSG
    for layer in range(1, G_size):
        for point in DSG.layer_dict[layer]:
            child_id_list = set()
            for child_id in point.child_id_set:
                if len(DSG.DSG_point_dict[child_id].parent_id_set) <= G_size \
                        and DSG.DSG_point_dict[child_id].layer-point.layer == 1:
                    child_id_list.add(child_id)
            point.child_id_set = set(child_id_list)

    # generate the groups
    list_point = 0
    while list_point < len(candidate_list):
        child_set = []
        group = list(candidate_list[list_point])
        last_p = group[len(group)-1]
        for point in group:
            for child_id in point.child_id_set:
                if (last_p.layer < DSG.DSG_point_dict[child_id].layer \
                    or (last_p.layer == DSG.DSG_point_dict[child_id].layer \
                        and last_p.layer_location < DSG.DSG_point_dict[child_id].layer_location)):
                    child_set.append(DSG.DSG_point_dict[child_id])
        g = []
        for i in child_set:
            g.append(i.id)
        g = set(g)
        child_set = []
        for i in g:
            child_set.append(DSG.DSG_point_dict[i])

        for child_point in child_set:
            for parent_id in child_point.parent_id_set:
                f = 0
                for point in group:
                    if parent_id == point.id:
                        f = 1
                        break
                if f == 0:
                    break
            if f:
                group.append(child_point)
                if len(group) < G_size:
                    candidate_list.append(group)
                if len(group) == G_size:
                    g_skyline.append(group)
                group = list(candidate_list[list_point])
        list_point += 1
    time2 = time.clock()

    return(g_skyline, time2 - time1, math.log10(time2 - time1 + 0.1 ** 10))

