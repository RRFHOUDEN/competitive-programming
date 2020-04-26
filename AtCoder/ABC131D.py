n = int(input())
ba = []
for i in range(n):
    a, b = map(int, input().split())
    ba.append([b, a])
ba.sort()
now = 0
out = 0
for i, j in ba:
    now += j
    if now > i:
        out = 1
        break
if out:
    print("No")
else:
    print("Yes")