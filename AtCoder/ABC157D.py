n, m, k = map(int, input().split())
connect = [[] for _ in range(n)]
cCnt = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    connect[a - 1].append(b - 1)
    cCnt[a - 1] += 1
    connect[b - 1].append(a - 1)
    cCnt[b - 1] += 1

group = [0 for _ in range(n)]
gNum = 0
import queue
for i in range(n):
    if group[i]:
        continue
    gNum += 1
    next = queue.Queue()
    for j in connect[i]:
        group[j] = gNum
        next.put(j)
    group[i] = gNum

    while not next.empty():
        j = next.get()
        group[j] = gNum
        for l in connect[j]:
            if not group[l]:
                group[l] = gNum
                next.put(l)

hunaka = [0 for i in range(n)]
for i in range(k):
    c, d = map(int, input().split())
    if group[c - 1] != group[d - 1]:
        continue
    hunaka[c - 1] += 1
    hunaka[d - 1] += 1

groupCnt = [0 for _ in range(gNum + 1)]
for i in group:
    groupCnt[i] += 1

for i in range(n):
    tmp = groupCnt[group[i]]
    tmp -= cCnt[i]
    tmp -= hunaka[i]
    tmp -= 1
    print(tmp, end = " ")
