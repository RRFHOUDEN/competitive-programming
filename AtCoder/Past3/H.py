n, l = map(int, input().split())
x = list(map(int, input().split()))
t = list(map(int, input().split()))
l += 1
dp = [10**10 for _ in range(l)]
dp[0] = 0
hardol = [0 for _ in range(l)]
for i in x:
    hardol[i] = 1

for i in range(l):
    if i == 0:
        continue
    p1 = 10**10
    p2 = 10**10
    p3 = 10**10

    if i >= 1:
        p1 = t[0] + dp[i-1]

    if i >= 2:
        p2 = t[0] + t[1] + dp[i-2]

    if i >= 4:
        p3 = t[0] + t[1] * 3 + dp[i-4]

    if hardol[i]:
        p1 += t[2]
        p2 += t[2]
        p3 += t[2]

    dp[i] = min(p1, p2, p3)

ans = dp[-1]

try:
    ans = min(ans, dp[-2]+0.5*t[0]+0.5*t[1])
except:
    pass
try:
    ans = min(ans, dp[-3]+0.5*t[0]+1.5*t[1])
except:
    pass
try:
    ans = min(ans, dp[-4]+0.5*t[0]+2.5*t[1])
except:
    pass

print(ans)