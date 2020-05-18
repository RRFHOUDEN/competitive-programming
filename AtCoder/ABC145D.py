def solve():
    x, y = map(int, input().split())
    n = (2*y-x) / 3
    m = (2*x-y) / 3

    mod = 10**9+7

    if n < 0 or m < 0 or (x+y)% 3 != 0:
        return 0
    cmb = 1
    n = int(n)
    m = int(m)

    cnt = 0
    for i in range(n):
        cnt += 1
        cmb *= n+m-i
        cmb *= pow(i+1, mod-2, mod)
        cmb %= mod
    return cmb

print(solve())