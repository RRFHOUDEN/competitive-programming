n, m = map(int, input().split())
work = [0 for _ in range(m)]
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))
ab.sort(key=lambda x:(x[0], -x[1]))
print(ab)
now = m-1
for a, b in ab:
    now = min(now, n-a+1)
    if now < 0:
        break
    print(now)
    work[now] = b
    now -= 1

print(work)
print(sum(work))