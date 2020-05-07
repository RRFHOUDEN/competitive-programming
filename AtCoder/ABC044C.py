n, a = map(int, input().split())
x = list(map(int, input().split()))

dp = [[[0 for _ in range(max(x)*n+1)] for _ in range(n)] for _ in range(n)]
x.sort()
for j in range(n+1):
    for k in range(n+1):
        for s in range(max(x)*n+1):
            if j == 0 and k == 0 and s == 0:
                dp[j][k][s] = 1
            elif j >= 1 and s < x[j]:
                dp[j][k][s] = dp[j-1][k][s]
            elif j >= 1 and k >= 1 and s >= x[j]:
                dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-x[j]]
            else:
                dp[j][k][s] = 0

ans = 0
for i in range(n):
    for j in range(1, n+1):
        ans += dp[i][j][j*a]

print(ans)