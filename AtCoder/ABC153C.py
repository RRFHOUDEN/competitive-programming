n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
h = h[::-1]
for i in range(k):
    if i >= n:
        break
    h[i] = 0
print(sum(h))