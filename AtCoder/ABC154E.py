import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def solve(k, m, i):
    if i >= len(dp):
        if k == 0:
            return 1
        else:
            return 0

    if i == 0:
        #n[i]
        ans = solve(k - 1, 1, i + 1)
        ans += (int(str(n)[i]) - 1) * solve(k - 1, 0, i + 1)
        return ans

    if k == 0 :
        return 1

    ans = 0
    if m == 1:
        if k > 0:
            ans = dp[i][2] * solve(k - 1, 0, i + 1)
            ans += solve(k - 1, 1, i + 1)
            ans += solve(k, 0, i + 1)
    else:
        if k > 0:
            ans = 9 * solve(k - 1, 0, i + 1)
            ans += solve(k, 0, i + 1)


    return ans

n = int(input())
k = int(input())

dp = [[0 for _ in range(3)] for _ in range(len(str(n)))]

# dp[i][0]...0のパターン
# dp[i][1]...1~9
# dp[i][2]...~n[i] - 1

for i in range(len(str(n))):
    dp[i][1] = 9
    dp[i][2] = int(str(n)[i]) - 1

ans = 0
ans += solve(k, 1, 0)
if len(str(n)) - 1 >= k:
    ans += combinations_count(len(str(n)) - 1, k) * 9 ** k

print(ans)