N, Y = map(int, input().split())
key = 0
for i in range(N + 1):
    for j in range(N - i + 1):
        if 1000 * i + 5000 * j + 10000 * (N - i - j) == Y:
            print(N - i - j, j, i)
            key = 1
            break
    if key:
        break
if not key:
    print(-1, -1, -1)