# -*-coding:utf-8-*-#
###############################
# 原文算法，无DSG剪枝
###############################
def UWise(G_size, test):
    import math

    g_skyline = []
    u_group_list = []
    u_group = []

    for layer in range(1,G_size+1):
        for item in test.layer_dict[layer]:
            if 0 <= len(item.parent_id_set) <= G_size - 1:
                u_group.append(item)
                if len(item.parent_id_set) > 0:
                    for parent_id in item.parent_id_set:
                        u_group.append(test.DSG_point_dict[parent_id])
                if len(u_group) == G_size:
                    g_skyline.append(u_group)
                if len(u_group) < G_size:
                    u_group_list.append(u_group)
                u_group = []

    for i in range(0, len(u_group_list)):
        for j in range(i, len(u_group_list)):
            if len(u_group_list[i]) < len(u_group_list[j]):
                sort = list(u_group_list[i])
                u_group_list[i] = list(u_group_list[j])
                u_group_list[j] = list(sort)

    candidate_u = list(u_group_list)
    sort = []
    for num in range(1, G_size+1):
        for point in candidate_u[len(candidate_u)-num]:
            sort.append(point.id)  #id only
        sort = list(set(sort))
        if len(sort) == G_size:
            break
    for i in range(1, num):
        candidate_u.pop()

    index = []
    for i in range(1, len(candidate_u)+1):
        index.append(i)

    list_p = 0
    while list_p < len(candidate_u):
        for i in range(index[list_p], len(u_group_list)):
            flag = 1
            PS = set()
            for j in candidate_u[list_p]:
                for parent_id in j.parent_id_set:
                    PS.add(parent_id)
            for j in PS:
                if u_group_list[i][0].id == test.DSG_point_dict[j].id:
                    flag = 0
                    break

            if flag:
                group = list(candidate_u[list_p])
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
                    candidate_u.append(group)
                    index.append(i+1)
                if len(group) == G_size:
                    g_skyline.append(group)
        list_p += 1

    return (g_skyline)
