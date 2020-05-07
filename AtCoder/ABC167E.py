import fractions
def combinations_count(n, r):
    return fractions.factorial(n) // (fractions.factorial(n - r) * fractions.factorial(r))
n, k = map(int, input().split())

cnt = [0 for _ in range(n)]
for i in range(1, n + 1):
    print(i)
    cnt[i - 1] = (k // i) ** n
    print(cnt[i - 1])

for i in range(1, n + 1):
    j = 2
    while i * j < n:
        print(i, j)
        cnt[i - 1] -= cnt[i * j - 1]
        j += 1

print(cnt)
ans = 0
for i in range(n):
    ans += cnt[i] * (i + 1) % (10 ** 9 + 7)
print(ans)