n = int(input())
d = list(map(int, input().split()))
d.sort()
ans = d[n // 2] - d[n // 2 - 1]

if n % 2 != 0:
    ans = 0
print(ans)