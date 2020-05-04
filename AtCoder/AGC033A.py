def make(i, j):
    if a[i][j] == ".":
        next_queue.put([i, j])
        visit[i][j] += 1
        a[i][j] = "#"
        return 0
    return 0

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
# print(a)
import queue
next_visit = queue.Queue()
visit = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            next_visit.put([i, j])

cnt = 0
while True:
    next_queue = queue.Queue()
    while not next_visit.empty():
        [i, j] = next_visit.get()
        if 0 < i:
            cnt += make(i-1, j)
        if 0 < j:
            cnt += make(i, j-1)
        if i < h-1:
            cnt += make(i+1, j)
        if j < w-1:
            cnt += make(i, j+1)
    next_visit = next_queue
    cnt += 1
    if next_queue.empty():
        break
print(cnt-1)
print(visit[0])

