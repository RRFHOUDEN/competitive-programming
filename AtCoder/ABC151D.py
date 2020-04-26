h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
disList = [[[[0 for _ in range(w)] for _ in range(h)] for _ in range(w)] for _ in range(h)]
# print(s)
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            visited[i][j] = 1
import copy

ans = 0
for i in range(h):
    for j in range(w):
        nowdis = 0
        now = 0
        next_point = [[i, j, nowdis]]
        thisVisited = copy.deepcopy(visited)
        thisVisited[i][j] = 1
        if s[i][j] == "#":
            continue

        while now < len(next_point):
            nowi = next_point[now][0]
            nowj = next_point[now][1]
            nowdis = next_point[now][2]
            disList[i][j][nowi][nowj] = nowdis

            if nowi != 0:
                if thisVisited[nowi - 1][nowj] == 0:
                    next_point.append([nowi - 1, nowj, nowdis + 1])
                    thisVisited[nowi - 1][nowj] = 1

            if nowi != h - 1:
                if thisVisited[nowi + 1][nowj] == 0:
                    next_point.append([nowi + 1, nowj, nowdis + 1])
                    thisVisited[nowi + 1][nowj] = 1

            if nowj != w - 1:
                if thisVisited[nowi][nowj + 1] == 0:
                    next_point.append([nowi, nowj + 1, nowdis + 1])
                    thisVisited[nowi][nowj + 1] = 1

            if nowj != 0:
                if thisVisited[nowi][nowj - 1] == 0:
                    next_point.append([nowi, nowj - 1, nowdis + 1])
                    thisVisited[nowi][nowj - 1] = 1
            now += 1

# print(disList)
ans = 0
for i in disList:
    for j in i:
        for k in j:
            # print(k)
            ans = max(ans, max(k))

print(ans)