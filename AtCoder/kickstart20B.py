t = int(input())
ans = []
for i in range(t):
    n, k, p = map(int, input().split())
    plate = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(k * p)] for _ in range(n)]
    for j in range(n):
        jP = 0
        nowP = plate[j][jP]
        for k in range(len(plate[j])):
            if j == 0:
                if k == 0:
                    dp[j][k] = plate[j][0]
                else:
                    dp[j][k] = dp[j][k - 1] + plate[j][k]
            else:
                if jP >= len(plate[j]):
                    dp[j][k] = max(dp[j - 1][k], dp[j][k - 1])
                else:
                    dp[j][k] = dp[j - 1][k]
                    if dp[j][k] < dp[j][k - 1] + plate[j][jP]:
                        1
    print(dp)