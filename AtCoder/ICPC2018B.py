ans_list = []
while True:
    n = int(input())
    if not n:
        break
    xy = []
    for i in range(n + 1):
        xy.append([])
        m = int(input())
        x, y = map(int, input().split())
        for j in range(m - 1):
            a, b = map(int, input().split())
            xy[i].append([a - x, b - y])


        if 0 > xy[i][0][0]:
            for j in range(m - 1):
                this = xy[i][j]
                xy[i][j] = [this[0] * -1, this[1] * -1]
        elif 0 < xy[i][0][1]:
            for j in range(m - 1):
                this = xy[i][j]
                xy[i][j] = [this[1], this[0] * -1]
        elif 0 > xy[i][0][1]:
            for j in range(m - 1):
                this = xy[i][j]
                xy[i][j] = [this[1] * -1, this[0]]

    ans = []
    import copy
    check1 = copy.copy(xy[0])
    check2 = []
    for i in check1[::-1]:
        check2.append([i[1], i[0]])
    check2 += [[0, 0]]
    for i in range(1, len(check2)):
        check2[i][0] = check2[i][0] - check2[0][0]
        check2[i][1] = check2[i][1] - check2[0][1]
        check2[i][1] *= -1

    del check2[0]
    m = len(check2) + 1
    if 0 > check2[0][0]:
        for j in range(m - 1):
            this = check2[j]
            check2[j] = [this[0] * -1, this[1] * -1]
    elif 0 < check2[0][1]:
        for j in range(m - 1):
            this = check2[j]
            check2[j] = [this[1], this[0] * -1]
    elif 0 > check2[0][1]:
        for j in range(m - 1):
            this = check2[j]
            check2[j] = [this[1] * -1, this[0]]

    for i in range(1, n + 1):
        if check1 == xy[i] or check2 == xy[i]:
            ans.append(i)
    ans.append("+++++")
    ans_list.append(ans)

for i in ans_list:
    for j in i:
        print(j)