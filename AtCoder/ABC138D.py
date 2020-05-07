import sys
sys.setrecursionlimit(2*(10**5)+1)

n, q = map(int, input().split())
tree = [[] for _ in range(n)] #tree = {i:{p:j, c:[k, l]}}
for i in range(n):
    tree[i] = [-1, [], 0]

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a-1][1].append(b-1)
    tree[b-1][0] = a-1

for i in range(q):
    p, x = map(int, input().split())
    tree[p-1][2] += x

x_list = [0 for _ in range(n)]

import queue
next_visit = queue.Queue()
next_visit.put(0)
while not next_visit.empty():
    i = next_visit.get()
    tmp = tree[i][2]
    if i != 0:
        tmp += x_list[tree[i][0]]
    x_list[i] = tmp
    for j in tree[i][1]:
        next_visit.put(j)

for i in x_list:
    print(i, end=" ")
