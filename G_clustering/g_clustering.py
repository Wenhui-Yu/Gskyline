########################################
# Fast UWise algorithm
# @ Wenhui Yu,
# E-mail: yuwh16@mails.tsinghua.edu.cn
#########################################

import random
import time
from distance import distance
import numpy as np
from Library import repre_output

class Cluster:
    def __init__(self, center, Dimension, G_size):
        self.center = center                        #np.array([[0] * Dimension] *  G_size)
        self.delta = np.zeros((G_size, Dimension))  #np.array([[0] * Dimension] *  G_size)
        self.num = 0

def g_clustering(g_skyline, G_size, Dimension, k, iter_num):
    time1 = time.clock()
    cluster_list = []
    #cluster_center = g_skyline[0]
    cluster_center = g_skyline[0]
    group_vector = []
    for point in cluster_center:
        group_vector.append(point.coordination)
    cluster = Cluster(np.array(group_vector), Dimension, G_size)
    cluster_list.append(cluster)

    # initialize the cluster centers
    for i in range(k - 1):
        dis_rec = 0
        index_rec = -1
        for index in range(len(g_skyline)):
            dis = 1
            for cluster in cluster_list:
                G = []
                for point in g_skyline[index]:
                    G.append(point.coordination)
                G = np.array(G)
                [d, u] = distance(G, cluster.center)
                dis *= d
            if dis > dis_rec:
                dis_rec = dis
                index_rec = index
        G = []
        for point in g_skyline[index_rec]:
            G.append(point.coordination)
        G = np.array(G)
        cluster = Cluster(G, Dimension, G_size)
        cluster_list.append(cluster)


    # start clustering
    cluster_num_rec = [-1] * k
    flag = 0
    num = 0
    while (flag < 2 and num < iter_num):
        num += 1
        # if to stop
        f = 1
        for i in range(k):
            if cluster_list[i].num != cluster_num_rec[i]:
                f = 0
                break
        if (f):
            flag += 1
        # update point number of each cluster
        for i in range(k):
            cluster_num_rec[i] = cluster_list[i].num
        # start iteration
        for cluster in cluster_list:
            cluster.delta = np.array([[0] * Dimension] *  G_size)
            cluster.num = 0
        for group in g_skyline:
            # generate vector for current group
            G = []
            for point in group:
                G.append(point.coordination)
            G = np.array(G)
            # find the cluster center of current group
            dis_cen = 100000
            u_cen = []
            G_cen = cluster_list[0].center
            cen = 0
            for i in range(len(cluster_list)):
                Gc = cluster_list[i].center
                [dis, u] = distance(G, Gc)
                if (dis_cen > dis):
                    dis_cen = dis
                    u_cen = u
                    G_cen = Gc
                    cen = i
            # calculate delta
            delta = []
            for i in range(G_size):
                point = []
                for j in range(Dimension):
                    point.append(G[u_cen[i]][j] - G_cen[i][j])
                delta.append(point)
            delta = np.array(delta)
            cluster_list[cen].delta = cluster_list[cen].delta + delta
            cluster_list[cen].num += 1
        for cluster in cluster_list:
            cluster.center += cluster.delta/cluster.num

    repre_group = []
    for cluster in cluster_list:
        Gc = cluster.center
        dis_rec = 10000
        group_cen = g_skyline[0]
        for group in g_skyline:
            G = []
            for point in group:
                G.append(point.coordination)
            G = np.array(G)
            [dis, u] = distance(G, Gc)
            if dis < dis_rec:
                dis_rec = dis
                group_cen = group
        repre_group.append(group_cen)
    time2 = time.clock()
    return (repre_group, time2 - time1)
