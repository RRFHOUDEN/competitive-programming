while 1:
    def solved(matrix):
        start = []
        import copy
        graf = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    start.append([i, j])
                graf[i][j] *= -1

        def BFS(graf, start, now):
            i, j = start[now]
            dis = graf[i][j]
            if i > 0:
                if graf[i - 1][j] == -1:
                    graf[i - 1][j] = dis + 1
                    start.append([i - 1, j])
            if j > 0:
                if graf[i][j - 1] == -1:
                    graf[i][j - 1] = dis + 1
                    start.append([i, j - 1])
            if j < len(graf[0]) - 1:
                if graf[i][j + 1] == -1:
                    graf[i][j + 1] = dis + 1
                    start.append([i, j + 1])
            if i < len(graf) - 1:
                if graf[i + 1][j] == -1:
                    graf[i + 1][j] = dis + 1
                    start.append([i+ 1, j])

            now += 1
            if now >= len(start):
                return graf
            return  BFS(graf, start, now)

        return BFS(graf, start, 0)

    matrix = [[0,0,0],
                [0,1,0],
                [1,1,1]]
    print(solved(matrix))
    break