while True:
    t, d, l = map(int, input().split())
    if not t and not d and not l:
        break

    data = [0 for i in range(t + d)]
    for i in range(t):
        x = int(input())
        if x >= l:
            data[i] += 1
            data[i + d - 1] -= 1

    ans = 0
    for i in range(len(data)):
        if i > 0:
            data[i] += data[i - 1]
        if data[i] > 0:
            ans += 1
    print(ans)
