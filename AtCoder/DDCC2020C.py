h, w, k = map(int, input().split())
s = [list(input()) for i in range(h)]
sikaku = [[0 for _ in range(w)] for _ in range(h)]
tmp = 0
key = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            if tmp == 0:
                tmp = key
            tmp += 1

        elif j == 0:
            if tmp != 0:
                key = tmp
            tmp = 0

        sikaku[i][j] = tmp

for i in range(h - 1, -1, -1):
    for j in range(w - 2, -1, -1):
        if sikaku[i][j] == 0:
            sikaku[i][j] = sikaku[i][j + 1]

for i in range(1, h):
    if sikaku[i][-1] == 0:
        for j in range(w):
            sikaku[i][j] = sikaku[i - 1][j]

for i in range(h - 2, -1, -1):
    if sikaku[i][-1] == 0:
        for j in range(w):
            sikaku[i][j] = sikaku[i + 1][j]

for i in range(h):
    for j in range(w):
        print(sikaku[i][j], end = " ")
    print()