import fractions
n = int(input())
a = list(map(int, input().split()))
if n <= 2:
    print(max(a))
else:
    gcd_left = [a[0]]
    gcd_right = [a[-1]]
    for i in range(1, n):
        gcd_left.append(fractions.gcd(a[i], gcd_left[-1]))
        gcd_right.append(fractions.gcd(a[n-i-1], gcd_right[-1]))
    gcd_right = gcd_right[::-1]
    # print(gcd_left, gcd_right)
    ans = max(gcd_left[-2], gcd_right[1])
    for i in range(n-2):
        ans = max(ans, fractions.gcd(gcd_right[i+2], gcd_left[i]))
    print(ans)