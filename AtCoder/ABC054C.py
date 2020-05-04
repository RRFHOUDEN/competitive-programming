def DFS(i):
    global ans
    ans += 1
    # print(ans)
    visited[i] = 0
    print(i, visited)
    if sum(visited) == 0:
        return 1
    cnt = 0
    for j in graf[i]:
        if visited[j] == 1:
            cnt += DFS(j)
    visited[i] = 1
    print(visited)
    return cnt

import sys
sys.setrecursionlimit(10 ** 9)
n, m = map(int, input().split())
graf = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graf[a-1].append(b-1)
    graf[b-1].append(a-1)

now = 0
visited = [1 for _ in range(n)]
visited[now] = 0
print(graf)
ans = 0
cnt = 0
for i in graf[now]:
    cnt += DFS(i)
print(cnt, visited)