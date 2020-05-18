import sys
sys.setrecursionlimit(10*5)

def f(i, j):
    tmp = 0
    if dp[i][j] != mod:
        return dp[i][j]

    if 0 < i:
        if a[i][j] < a[i-1][j]:
            tmp += f(i-1, j) + 1
    if i < h-1:
        if a[i][j] < a[i+1][j]:
            tmp += f(i+1, j) + 1
    if 0 < j:
        if a[i][j] < a[i][j-1]:
            tmp += f(i, j-1) + 1
    if j < w-1:
        if a[i][j] < a[i][j+1]:
            tmp += f(i, j+1) + 1
    return tmp

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
mod = 10**9+7
dp = [[mod for _ in range(w)] for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        dp[i][j] = (f(i, j) + 1) % mod
        ans += dp[i][j] % mod
        print(dp)
print(ans)
tmp = 0
for i in dp:
    for j in i:
        tmp += j
print(tmp)
print(dp)
