n = int(input())
p = list(map(int, input().split()))

maxP = [p[0]]
for i in range(1, n):
    maxP.append(min(maxP[i - 1], p[i]))


ans = 0
for i in range(n):
    if p[i] <= maxP[i]:
        ans += 1

print(ans)