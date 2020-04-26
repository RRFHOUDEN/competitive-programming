while True:
    break
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    tile = []
    for i in range(h):
        tile.append(list(input()))

    for i in range(h):
        for j in range(w):
            if tile[i][j] == "@":
                start = [i, j]
                break

    canlist = [[0 for i in range(w)] for j in range(h)]

    def sarch(graf, starti, startj):
        canlist[starti][startj] = 1
        if 0 < i:
            if canlist[starti - 1][startj] == 0 and tile[starti - 1][startj]:
                canlist[starti - 1][startj] = 1
                sarch(graf, starti - 1, startj)
        if i < len(graf):
            1

