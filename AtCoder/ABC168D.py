n, m = map(int, input().split())
graf = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graf[a-1].append(b-1)
    graf[b-1].append(a-1)

out = [0 for _ in range(n)]
out[0] = -1

import queue

next_visit = queue.Queue()
next_visit.put(0)

while not next_visit.empty():
    i = next_visit.get()
    for j in graf[i]:
        if out[j] == 0:
            out[j] = i+1
            next_visit.put(j)
cnt = 1

for i in range(1, n):
    if out[i] == 0:
        cnt = 0
        break
if cnt:
    print("Yes")
    for i in out[1:]:
        print(i)
else:
    print("No")