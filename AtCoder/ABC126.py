def BFS(root, now, dis):
    for i in root[now]:
        if (dis + i[1]) % 2 == 0:
            color[i[0]] = color[start]

n = int(input())
uvw = [list(map(int, input().split())) for i in range(n - 1)]
root = [[] for i in range(n)]
color = [1 for i in range(n)]
for u, v, w in uvw:
    root[u - 1].append(v - 1)

BFS(root, 0)

print(color)
print(root)