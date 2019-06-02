# -*- coding: utf-8 -*-
def pruning_tree(D, n, Th):
    global th
    th = Th
    a = []
    for i in range(n):
        a.append(i + 1)
    x = [0] * n  # 一个解（n元0-1数组）

    # 用子集树模板实现全排列
    def perm(k, sum):  # 到达第k个元素
        global th
        d = 0
        if k > 0:
            d = D[k - 1][x[k - 1] - 1]
        sum += d
        #print(x, sum, th),
        if k >= n:  # 超出最尾的元素
            if sum < th:
                th = sum
        else:
            for i in set(a) - set(x[:k]):  # 遍历，剩下的未排的所有元素看作元素x[k-1]的状态空间
                x[k] = i
                if sum < th:  # 剪枝
                    perm(k + 1, sum)
    perm(0, 0)  # 从x[0]开始
    return th
