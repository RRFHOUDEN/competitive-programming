n, m, q = map(int, input().split())
scores = [[0 for _ in range(m)] for _ in range(n)]
points = [n for _ in range(m)]
for i in range(q):
    s = list(map(int, input().split()))
    # print(i, scores)
    if len(s) == 2:
        point = 0
        for i in range(m):
            if scores[s[1]-1][i]:
                point += max(0, points[i])

        print(point)
    else:
        scores[s[1]-1][s[2]-1] = 1
        points[s[2]-1] -= 1