########################################
# Fast UWise algorithm
# @ Wenhui Yu
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

import time
import math

def F_UWise(G_size, DSG):
    time.clock()
    time1 = time.clock()

    candidate_list = []
    group = []
    g_skyline = []

    for point in DSG.layer_dict[1]:
        group.append(point)
        candidate_list.append(group)
        group = []

    '''list_point = 0
    while list_point < len(candidate_list):
        group = list(candidate_list[list_point])
        if len(group) < G_size - 1:
            for i in range(group[len(group) - 1].layer_location + 1, len(DSG.layer_dict[1])):
                group.append(DSG.layer_dict[1][i])
                candidate_list.append(group)
                group = list(candidate_list[list_point])
        list_point += 1'''

    u_group_list = []
    u_group = []
    group = []
    for layer in range(1,G_size+1):
        for item in DSG.layer_dict[layer]:
            if len(item.parent_id_set) <= G_size - 1:
                u_group.append(item)
                for parent_id in item.parent_id_set:
                    u_group.append(DSG.DSG_point_dict[parent_id])
                if len(u_group) == G_size:
                    g_skyline.append(u_group)
                if len(u_group) < G_size:
                    u_group_list.append(u_group)
                u_group = []

    sort = []
    for i in range(0, len(u_group_list)):
        for j in range(i, len(u_group_list)):
            if len(u_group_list[i]) < len(u_group_list[j]):
                sort = list(u_group_list[i])
                u_group_list[i] = list(u_group_list[j])
                u_group_list[j] = list(sort)

    candidate_list = list(u_group_list)

    index = []
    for i in range(1, len(candidate_list)+1):
        index.append(i)

    list_p = 0
    while list_p < len(candidate_list):
        if len(candidate_list[list_p]) > 1:
            for i in range(index[list_p], len(u_group_list)):
                flag = 1

                for j in candidate_list[list_p]:
                    if u_group_list[i][0].id == j.id:
                        flag = 0
                        break

                if flag:
                    group = list(candidate_list[list_p])
                    group += u_group_list[i]
                    g = []
                    g.append(group[0])
                    for ii in group:
                        flag = 1
                        for jj in g:
                            if ii.id == jj.id:
                                flag = 0
                        if flag:
                            g.append(ii)
                    group = list(g)

                    if len(group) < G_size:
                        candidate_list.append(group)
                        index.append(i+1)
                    if len(group) == G_size:
                        g_skyline.append(group)
        list_p += 1
    time2 = time.clock()
    return (g_skyline, time2 - time1, math.log10(time2 - time1 + 0.1 ** 10))

