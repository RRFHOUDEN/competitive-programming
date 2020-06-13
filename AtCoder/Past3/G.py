def check(i, j):
    if not(-250 <= i <= 250) or not(-250 <= j <= 250):
        return True
    return str(i)+"+"+str(j) in obastacle_set

n, x, y = map(int, input().split())
obastacle = [list(map(int, input().split())) for _ in range(n)]
obastacle_set = set()

for i, j in obastacle:
    obastacle_set.add(str(i)+"+"+str(j))

from collections import deque
next_visit = deque()
next_visit.append([0, 0, 0])
i, j = 0, 0
cnt = 0
# print(obastacle_set)
while len(next_visit) > 0:
    i, j, cnt = next_visit.popleft()
    obastacle_set.add(str(i)+"+"+str(j))
    # print(i, j)
    if i == x and j == y:
        break
        
    if not check(i+1, j+1):
        next_visit.append([i+1, j+1, cnt+1])
        obastacle_set.add(str(i+1) + "+" + str(j+1))

    if not check(i, j+1):
        next_visit.append([i, j+1, cnt+1])
        obastacle_set.add(str(i) + "+" + str(j+1))

    if not check(i-1, j+1):
        next_visit.append([i-1, j+1, cnt+1])
        obastacle_set.add(str(i-1) + "+" + str(j+1))

    if not check(i+1, j):
        next_visit.append([i+1, j, cnt+1])
        obastacle_set.add(str(i+1) + "+" + str(j))

    if not check(i-1, j):
        next_visit.append([i-1, j, cnt+1])
        obastacle_set.add(str(i-1) + "+" + str(j))

    if not check(i,j-1):
        next_visit.append([i, j-1, cnt+1])
        obastacle_set.add(str(i) + "+" + str(j-1))

if i == x and j == y:
    print(cnt)
else:
    print(-1)