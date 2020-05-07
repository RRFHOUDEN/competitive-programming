n, m = map(int, input().split())

dp = [[10 ** 20 for _ in range(n)] for _ in range(m)]

for i in range(m):
    s, c = input().split()
    c = int(c)
    for j in range(n):
        if s[j] == "Y":
            dp[i][j] = c
        else:
            break
    # print(dp)
    for j in range(n):
        if i == 0:
            if s[j] == "Y":
                dp[i][j] = c
        else:
            dp[i][j] = min(dp[i][j], dp[i-1][j])

            if j != 0 and s[j] == "Y":
                dp[i][j] = min(dp[i-1][j-1] + c, dp[i][j])

for i in dp:
    print(i)

if dp[-1][-1] >= 10 ** 20:
    print(-1)
else:
    print(dp[-1][-1])