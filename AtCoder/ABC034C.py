w, h = map(int, input().split())
dp = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if i == 0:
            dp[i][j] = 1
            continue
        if j == 0:
            dp[i][j] = 1
            continue
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % (10**9+7)

print(dp[-1][-1])