while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    flower = [i for i in range(7368792)]
    now = m
    dellist = []
    for i in range(n):
        j = now
        while j < len(flower):
            flower[j] = 1
            j += now
        now += 1
        #print(now)
        while flower[now] > 0:
            now += 1
    print(now)
    #print(flower[:20])