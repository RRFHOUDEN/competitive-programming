h, n = map(int, input().split())
a = []
b = []
for i in range(n):
    ia, ib = map(int, input().split())
    a.append(ia)
    b.append(ib)

dp = [[0 for i in range(h)] for j in range(n)]

for i in range(n):
    for j in range(h):
        if i == 0:
            tmp = (j + 1) // a[i]
            if tmp != (j + 1) / a[i]:
                tmp += 1
            dp[i][j] = tmp * b[i]
        else:
            if j != 0:
                if j - a[i] < 0:
                    tmp = b[i]
                else:
                    tmp = dp[i][j - a[i]] + b[i]
                dp[i][j] = min(dp[i - 1][j], tmp)
            else:
                tmp = (j + 1) // a[i]
                if tmp != (j + 1) / a[i]:
                    tmp += 1
                dp[i][j] = min(dp[i - 1][j], tmp * b[i])

print(dp[-1][-1])