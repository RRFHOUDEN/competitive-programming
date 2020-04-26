from collections import deque
INF = 10 ** 10

def search(nowi, nowj, next, root, yoko, tate):
    global INF
    if nowi == h - 1 and nowj == w - 1:
        return root[nowi][nowj]
    # print(nowi, nowj, len(yoko), len(tate), h, w, yoko, tate)
    dis = root[nowi][nowj]
    if 0 < nowi:
        if root[nowi - 1][nowj] == INF and tate[nowi - 1][nowj] == 0:
            next.append([nowi - 1, nowj])
            root[nowi - 1][nowj] = dis + 1
    if 0 < nowj:
        if root[nowi][nowj - 1] == INF and yoko[nowi][nowj - 1] == 0:
            next.append([nowi, nowj - 1])
            root[nowi][nowj - 1] = dis + 1
    if nowi < len(root) - 1:
        if root[nowi + 1][nowj] == INF and tate[nowi][nowj] == 0:
            next.append([nowi + 1, nowj])
            root[nowi + 1][nowj] = dis + 1 
    if nowj < len(root[nowi]) - 1:
        if root[nowi][nowj + 1] == INF and yoko[nowi][nowj] == 0:
            next.append([nowi, nowj + 1])
            root[nowi][nowj + 1] = dis + 1
    if len(next) == 0:
        return 0
    nextij = next.popleft()
    nexti = nextij[0]
    nextj = nextij[1]
    return search(nexti, nextj, next, root, yoko, tate)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    yoko = []
    tate = []

    for i in range(2 * h - 1):
        if i % 2 == 0:
            yoko.append(list(map(int, input().split())))
        else:
            tate.append(list(map(int, input().split())))
    
    root = [[INF for _ in range(w)] for _ in range(h)]
    root[0][0] = 1
    next = deque()
    print(search(0, 0, next, root, yoko, tate))
    