n, w = map(int, input().split())
vw = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for _ in range(n * 1000 + 1)] for _ in range(n + 1)]
for i in range(len(dp)):
    for j in range(len(dp[i])):
        if i == 0 and j == 0:
            dp[i][j] = 0
        elif i == 0:
            dp[i][j] = -100000
        else:
            if j - vw[i - 1][1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - vw[i - 1][1]] + vw[i - 1][0])
            else:
                dp[i][j] = dp[i - 1][j]

ans = 0
for i in range(len(dp)):
    for j in range(min(w + 1, len(dp[i]))):
        ans = max(ans, dp[i][j])
#print(ans)

dp2 = [[0 for _ in range(n * 1000 + 1)] for _ in range(n + 1)]
dp2[0][0] = 0
for i in range(len(dp2)):
    for j in range(len(dp2[i])):
        if i == 0 and j == 0:
            dp2[i][j] = 0
        elif i == 0:
            dp2[i][j] = 10000000000000
        else:
            if j - vw[i - 1][0] >= 0:
                dp2[i][j] = min(dp2[i - 1][j], dp2[i - 1][j - vw[i - 1][0]] + vw[i - 1][1])
            else:
                dp2[i][j] = dp2[i - 1][j]

ans2 = 0
for i in range(len(dp2)):
    for j in range(len(dp2[i])):
        if dp2[i][j] <= w:
            ans2 = max(ans2, j)
print(max(ans, ans2))