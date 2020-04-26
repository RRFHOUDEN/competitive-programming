h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

countL2R = [[0 for i in range(w)] for j in range(h)]
countR2L = [[0 for i in range(w)] for j in range(h)]
countU2D = [[0 for i in range(w)] for j in range(h)]
countD2U = [[0 for i in range(w)] for j in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            countL2R[i][j] = -1
            countR2L[i][j] = -1
            countU2D[i][j] = -1
            countD2U[i][j] = -1

for i in range(h):
    for j in range(w):
        if j > 0 and countL2R[i][j] != -1:
                countL2R[i][j] = countL2R[i][j - 1] + 1

        j = w - j - 1
        if j < w - 1 and countR2L[i][j] != -1:
            countR2L[i][j] = countR2L[i][j + 1] + 1

        if i > 0 and countU2D[i][j] != -1:
            countU2D[i][j] = countU2D[i - 1][j] + 1

        I = i
        i = h - i - 1
        if i < h - 1 and countD2U[i][j] != -1:
            countD2U[i][j] = countD2U[i + 1][j] + 1
        i = I

ans = 0
for i in range(h):
    for j in range(w):
        if countD2U[i][j] != -1:
            ans = max(ans, countD2U[i][j] + countU2D[i][j] + countR2L[i][j] + countL2R[i][j])

print(ans + 1)