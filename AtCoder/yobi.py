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
print(ans)