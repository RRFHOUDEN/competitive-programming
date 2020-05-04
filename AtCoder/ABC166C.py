

n, m = map(int, input().split())
h = list(map(int, input().split()))
good = [1 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if h[a-1] == h[b-1]:
        good[a-1] = 0
        good[b-1] = 0
    elif h[a-1] > h[b-1]:
        good[b-1] = 0
    elif h[a-1] < h[b-1]:
        good[a-1] = 0
print(sum(good))