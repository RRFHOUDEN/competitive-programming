def solved():
    a = [input() for _ in range(10)]
    island = [[0 for _ in range(10)] for _ in range(10)]
    i_num = 1
    import queue
    for i in range(10):
        for j in range(10):
            if a[i][j] == "o" and island[i][j] == 0:
                next_visit = queue.Queue()
                next_visit.put([i, j])
                island[i][j] = i_num
                while not next_visit.empty():
                    # print(i, j)
                    [i, j] = next_visit.get()
                    if 0 < i and a[i-1][j] == "o" and island[i-1][j] == 0:
                        next_visit.put([i-1, j])
                        island[i-1][j] = i_num
                    if 0 < j and a[i][j-1] == "o" and island[i][j-1] == 0:
                        next_visit.put([i, j-1])
                        island[i][j-1] = i_num
                    if i < 9 and a[i+1][j] == "o" and island[i+1][j] == 0:
                        next_visit.put([i+1, j])
                        island[i+1][j] = i_num
                    if j < 9 and a[i][j+1] == "o" and island[i][j+1] == 0:
                        next_visit.put([i, j+1])
                        island[i][j+1] = i_num
                i_num += 1


    if i_num < 2:
        print("YES")
        return
    # print(i_num)
    for i in range(10):
        for j in range(10):
            tmp = []
            if 0 < i:
                tmp.append(island[i-1][j])
            if 0 < j:
                tmp.append(island[i][j-1])
            if i < 9:
                tmp.append(island[i+1][j])
            if j < 9:
                tmp.append(island[i][j+1])
            can = 1
            # print(i, j, tmp)
            for k in range(1, i_num):
                if not k in tmp:
                    can = 0
            if can:
                print("YES")
                return
            # print(i, j, tmp)
    print("NO")
    return
solved()