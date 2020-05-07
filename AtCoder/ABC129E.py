import fractions


def combinations_count(n, r):
    return fractions.factorial(n) // (fractions.factorial(n - r) * fractions.factorial(r))


l = int(input())
L = l
ans = 0

L = str(L)
cnt = 0
for i in range(len(L)):
    if L[i] == "1":
        l = len(L) - i - 1
        print(l)
        if l > 0:
            cnt = 1
            for j in range(l + 1):
                # print(l, j, (combinations_count(l, j)), i)
                ans += ((combinations_count(l, j) * 2 ** max(0, l - j))) % (10 ** 9 + 7)

print(ans)
if cnt == 0:
    l = len(L)
    for i in range(l + 1):
        ans += (combinations_count(l, i) * (2 ** (l - i)) % (10 ** 9 + 7))
        print((combinations_count(l, i) * (2 ** (l - i)) % (10 ** 9 + 7)))

ans += 2
print(ans)
