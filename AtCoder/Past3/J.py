n, m = map(int, input().split())
a = list(map(int, input().split()))
eats = [0 for _ in range(n)]
import bisect
for i in a:
    i *= -1
    num = bisect.bisect_right(eats, i)
    # print(i, num, eats)
    if num >= n:
        print(-1)
    else:
        print(num+1)
        eats[num] = i