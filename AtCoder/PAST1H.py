n = int(input())
c = list(map(int, input()))
odd = 10 ** 10
all = 10 ** 10
for i in range(n):
    if i % 2 == 0:
        odd = min(c[i], odd)
    all = min(all, c[i])

q = int(input())
ans = 0
odd_buy = 0
buy = 0
for i in range(q):
    s = list(input().split())
    if len(s) == 3:
        if c[int(s[1])] - odd_buy - buy > int(s[2]):
            ans += int(s[2])
            c[int(s[1])] -= int(s[2])
            if int(s[2]) % 2 == 0:
                odd = min(odd, c[int(s[2])])

    else:
        if int(s[0]) == 2:
            if odd - odd_buy - buy >= int(s[1]):
                odd_buy += int(s[1])
                ans += int(s[1]) * (n // 2)
        else:
            if all - buy >= 1:
                pass