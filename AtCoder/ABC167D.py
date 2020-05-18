n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1

visited = [0 for _ in range(n)]
i = 0
while visited[i] == 0:
    visited[i] = 1
    i = a[i]

cnt = 0
goal = i
i = goal
while not (i == goal and cnt > 0):
    i = a[i]
    cnt += 1

i = 0

if True:
    while i != goal and k > 0:
        k -= 1
        i = a[i]
    if k != 0:

        k = k % cnt
        i = goal

        for cnt in range(k):
            i = a[i]

print(i+1)