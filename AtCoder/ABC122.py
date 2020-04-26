N = int(input())

dp = [[0 for i in range(16)] for j in range(N)]
dp2 = [[0 for j in range(4)] for j in range(N)]
for i in range(16):
    dp[1][i] = 1

dp[2] = [4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4]

for i in range(2, N):

    DP = dp[i - 1]
    dp[i][0] = DP[0] + DP[4] + DP[8] + DP[12]
    dp[i][1] = DP[0] + DP[4] + DP[8] + DP[12]
    dp[i][2] = DP[0] + DP[8] + DP[12]
    dp[i][3] = DP[0] + DP[4] + DP[8] + DP[12]
    dp[i][4] = DP[1] + DP[5] + DP[9] + DP[13]
    dp[i][5] = DP[1] + DP[5] + DP[9] + DP[13]
    dp[i][6] = DP[5] + DP[9] + DP[13]
    dp[i][7] = DP[1] + DP[5] + DP[9] + DP[13]
    dp[i][8] = DP[2] + DP[6] + DP[10] + DP[14]
    dp2[i][0] = DP[6] + DP[10] + DP[14]
    dp[i][9] = DP[6] + DP[10] + DP[14] - dp2[i - 1]
    dp2[i][1] = DP[]
    dp[i][10] = DP[2] + DP[6] + DP[10] + DP[14]
    dp[i][11] = DP[2] + DP[6] + DP[10] + DP[14]
    dp[i][12] = DP[3] + DP[7] + DP[11] + DP[15]
    dp[i][13] = DP[3] + DP[7] + DP[11] + DP[15]
    dp[i][14] = DP[3] + DP[7] + DP[11] + DP[15]
    dp2[i] = DP[3]
    dp[i][15] = DP[3] + DP[7] + DP[11] + DP[15]

print(sum(dp[-1]) % (10 ** 9 + 7))
print(dp)