def sarch(n, l):
    a = n * 10 + 5
    b = n * 10
    if l - 1 > 0:
        ans = sarch(a, l - 1)
        ans += sarch(b, l - 1)
    else:
        ans = 0
    # print(a, b)
    while n % 5 == 0 and n > 0:
        # print(n, 2)
        ans += 1
        n //= 5
    # print(n)
    return ans

n = int(input())
if n % 2 == 0:
    ans = 0
    tmp = 10
    while tmp <= n:
        ans += n // tmp
        tmp *= 5
    print(ans)
else:
    print(0)