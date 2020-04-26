cnt = 0
while True:
    d, w = map(int, input().split())
    if d == 0 and w == 0:
        break

    e = [list(map(int, input().split())) for i in range(d)]
    V = 0
    for i_l in range(d - 2):
        for i_r in range(min(i_l + 2, d), d):
            for j_l in range(w - 2):
                for j_r in range(min(j_l + 2, w), w):
                    min_out = 10 ** 10
                    max_in = 0
                    tmp = 0
                    for i in range(i_l, i_r + 1):
                        for j in range(j_l, j_r + 1):
                            if i == i_l or i == i_r or j == j_l or j == j_r:
                                #print(i, j)
                                min_out = min(min_out, e[i][j])
                            else:
                                max_in = max(max_in, e[i][j])

                    for i in range(i_l, i_r + 1):
                        for j in range(j_l, j_r + 1):
                            if min_out > max_in:
                                if i == i_l or i == i_r or j == j_r or j == j_l:
                                    1
                                else:
                                    #print(i_l, i_r, j_l, j_r, i, j, min_out, max_in, e[i][j])
                                    tmp += min_out - e[i][j]


                    #print(tmp)
                    V = max(tmp, V)

    print(V)