n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

if n < m:
    s, t = t, s
    n, m = m, n
#n >>> m
# tmp = [0 for _ in range(max(n, m))]
tmp = []

for i in range(n):
    thistmp = []
    for j in range(min(n - i, m)):
        thistmp.append(s[i + j] - t[j])
    tmp.append(thistmp)

for i in range(1, n):
    thistmp = []
    for j in range(m + i - n, m):
        thistmp.append(s[j - i] - t[j])
    tmp.append(thistmp)
print(tmp)