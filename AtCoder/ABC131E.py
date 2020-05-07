import fractions
def combinations_count(n, r):
    return fractions.factorial(n) // (fractions.factorial(n - r) * fractions.factorial(r))

n, k = map(int, input().split())
ans = 0
if n == 2:
    if k == 0:
        print(1)
        print(1, 2)
    else:
        ans = -1
else:
    if k > combinations_count(n - 1, 2):
        ans = -1
    else:
        print(combinations_count(n - 1, 2) - k + n - 1)
        delcnt = combinations_count(n - 1, 2) - k
        cnt = 0
        # print(combinations_count(n - 1, 2), delcnt)
        for i in range(2, n + 1):
            if cnt >= delcnt:
                break
            for j in range(i + 1, n + 1):
                print(i, j)
                cnt += 1
                if cnt >= delcnt:
                    break
            if cnt >= delcnt:
                break
        for i in range(1, n):
            print(1, i + 1)

if ans == -1:
    print(ans)