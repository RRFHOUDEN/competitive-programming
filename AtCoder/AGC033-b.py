n, m = map(int, input().split())
datalist = [0 for i in range(n)]
ans = 0
root = [[] for i in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    root[x - 1].append(y - 1)
    root[y - 1].append(x - 1)

def solve(now):
    global ans, root
    if datalist[now] == 0:
        ans += 1
    datalist[now] = 1
    for j in range(len(root[now])):
        if not datalist[root[now][j]]:
            datalist[root[now][j]] = 1
            solve(root[now][j])

for i in range(n):
    if not datalist[i]:
        solve(i)

for i in datalist:
    if i == 0:
        ans += 1

print(ans)