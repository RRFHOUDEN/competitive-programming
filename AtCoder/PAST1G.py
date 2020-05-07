def make_group(cnt, now):
    if cnt == 0:
        group.append(now)
        return
    make_group(cnt-1, now+[0])
    make_group(cnt-1, now+[1])
    make_group(cnt-1, now+[2])

n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n-1):
    ai = list(map(int, input().split()))
    for j in range(n-i-1):
        aij = ai[j]
        a[i][j+i+1] = aij
        a[j+i+1][i] = aij

group = []
make_group(n, [])
group.sort()
ans = -10 ** 10
for i in group:
    tmp = 0
    groups = [[], [], []]
    for j in range(n):
        groups[i[j]].append(j)
    for j in groups:
        for k in j:
            for l in j:
                if k < l:
                    tmp += a[l][k]
    ans = max(tmp, ans)
print(ans)