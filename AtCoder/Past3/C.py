a, r, n = map(int, input().split())
if r == 1:
    print(a*r**(n-1))
else:
    ans = a
    for i in range(n-1):
        a *= r
        if a > 10**9:
            break
    if a > 10**9:
        print("large")
    else:
        print(a)