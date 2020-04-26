n, m = map(int, input().split())
a = list(map(int, input().split()))
suma = sum(a)
cnt = 0
for i in a:
    if not i < suma / 4 / m:
        cnt += 1

if cnt >= m:
    print("Yes")
else:
    print("No")