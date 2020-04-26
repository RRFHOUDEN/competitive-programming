t = int(input())

num = 0
while num < t:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n - 1):
        tmp = i + k + 1
        if a[i] != a[i + 1]:
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    if j - i - 1 <= k:
                        tmp = min(j, tmp)
        else:
            tmp = i

        print(i, tmp, a, k)
        for j in range(i + 1, min(tmp, n)):
            a[j] = a[i]
        if i != tmp:
            k -= tmp - i - 1

    for i in range(1, n - 1): #+2
        if a[i - 1] != a[i] and a[i] != a[i] and a[i - 1] == a[i + 1] and k > 0:
            a[i] = a[i - 1]

    print(k)
    if k > 0 and a[0] != a[1]:
        a[0] = a[1]
        k -= 1
    if k > 0 and a[-1] != a[-2]:
        a[-1] = a[-2]

    ans = 0
    for i in range(1, n):
        if a[i] != a[i - 1]:
            ans += 1

    print(ans)
    print(a)