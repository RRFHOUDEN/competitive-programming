def prime_factorize(a, n):
    now = len(a) - 1
    while n % 2 == 0:
        if now == -1:
            a.append(2)
            now += 1
        elif a[now] != 2:
            a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if now == -1:
                a.append(f)
                now += 1
            elif a[now] != f:
                a.append(f)
                now += 1
            n //= f
        else:
            f += 2

    if n != 1:
        if now == -1:

            a.append(f)
        elif a[now] != n:

            a.append(n)
    return a

n = int(input())
a = list(map(int, input().split()))
a.sort()

i = 0
ans = 0
for i in range(n - 1):
    if a[i] == a[i + 1]:
        ans = 1
        break
if ans:
    print("NO")
else:
    print("YES")