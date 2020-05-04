n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
ans = 0
for i in range(n):
    if i + a[i] < n:
        dp[i+a[i]] += 1
    if 0<= i-a[i]:
        ans += dp[i-a[i]]
# print(dp)
print(ans)