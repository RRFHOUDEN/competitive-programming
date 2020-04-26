n, x = map(int, input().split())
l = list(map(int, input().split()))
d = [0]
for i in range(n):
    d.append(d[i] + l[i])
ans = 0
for i in d:
    if i <= x:
        ans += 1
print(ans)