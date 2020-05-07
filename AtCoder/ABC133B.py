import math
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        tmp = 0
        for k in range(d):
            tmp += (x[i][k] - x[j][k]) ** 2
        tmp = math.sqrt(tmp)
        if tmp == int(tmp):
            cnt += 1
print(cnt)