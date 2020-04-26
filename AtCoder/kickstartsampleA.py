t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    now = b
    n = int(input())
    cnt = 0
    while True:
        cnt += 1
        print(now)
        s = input()
        if s == "TOO_BIG":
            b = now
            now = (a + now) // 2

        elif s == "TOO_SMALL":
            a = now
            now = (now + b) // 2

        elif s == "CORRECT":
            break

        elif s == "WRONG_ANSER":
            break
        if cnt >= n:
            break