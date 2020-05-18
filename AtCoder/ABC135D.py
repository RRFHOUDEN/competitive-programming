s = input()
s = s[::-1]
dp = [[0 for _ in range(13)] for _ in range(len(s))]

for i in range(len(s)):
    if i == 0:
        if s[i] == "?":
            for j in range(10):
                dp[0][j] = 1
        else:
            dp[0][int(s[0])] = 1
    else:
        if s[i] == "?":
            for j in range(10):
                for k in range(10):
                    # if i == 2:
                    #     print((j * (10 ** i) + k), (j * (10 ** i) + k), (j * (10 ** i) + k) % 13, dp[i-1][k])
                    dp[i][(j * (10 ** i) + k) % 13] += dp[i-1][k]
        else:
            for j in range(10):
                dp[i][(int(s[i]) * (10 ** i) + j) % 13] = dp[i-1][j]

print(dp)
print(dp[-1][5])