def perm(l):
    if (len(l) <= 1):
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i + 1] + x)
    return r

def true_distance(D, k):
    index = []
    for i in range(k):
        index.append(i)

    index_perm_list = perm(index)
    true_dis = 100000000000000
    for index_perm in index_perm_list:
        sum_dis = 0
        for i in range(k):
            sum_dis += D[i][index_perm[i]]
        if sum_dis < true_dis:
            true_dis = sum_dis
    return true_dis