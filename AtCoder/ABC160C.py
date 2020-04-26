k, n = map(int, input().split())
a = list(map(int, input().split()))
maxdis = 0
for i in range(1, n):
    maxdis = max(maxdis, a[i] - a[i - 1])
maxdis = max(maxdis, a[0] + k - a[-1])
print(k - maxdis)