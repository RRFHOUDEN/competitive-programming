n, k, m = map(int, input().split())
a = list(map(int, input().split()))

target = m * n
for i in a:
    target -= i
if target > k:
    print(-1)
else:
    print(max(0, target))