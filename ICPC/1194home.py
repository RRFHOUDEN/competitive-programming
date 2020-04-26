import math
while True:
    r, n = map(int, input().split())
    if r == 0 and n == 0:
        break
    sun_time = [-10 ** 10 for i in range(200)]
    for i in range(r):
        tmp = -r + math.sqrt(r * r - i * i)
        sun_time[100+ i] = tmp
        sun_time[99 - i] = tmp
    # print(sun_time)
    # for i in range(1, 2 * r + 1):
    #     for j in range(200):
    #         sun_time[i][j] = sun_time[i - 1][j] + 1

    bilding = [0 for i in range(200)]
    ans = 100000000000000000
    for i in range(n):
        xl, xr, h = map(int, input().split())
        for j in range(xl, xr):
            bilding[100 + j] = h

    for i in range(200):
        ans = min(ans, bilding[i] - sun_time[i])

    print(ans)