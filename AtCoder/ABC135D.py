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
                    dp[i][(j * 10 ** (i+1) + dp[i-1][j]) % 13] = dp[i-1][j]
        else:
            dp[i][(int(s[i]) * 10 ** (i+1) + dp[i-1][j]) % 13]