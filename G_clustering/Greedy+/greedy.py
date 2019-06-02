def greedy(D, k):
    b = []
    for i in range(k):
        for j in range(k):
            b.append((D[i][j],(i,j)))
    b.sort(key=lambda x: x[0])
    num = 0
    sum_dis = 0
    row = []
    for i in range(k):
        row.append(k)
    column = list(row)
    for (dis,(x, y)) in b:
        if row[x] == k and column[y] == k:
            sum_dis += dis
            num += 1
            row[x] -= 1
            column[y] -= 1
        if num == k:
            break
    return sum_dis
