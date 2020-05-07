import fractions
def permutations_count(n, r):
    if r != n:
        return F[n] // F[r] // F[n - r]
    return 1
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
K = fractions.factorial(k)
# print(a)
F = [1 for i in range(10**5 + 1)]
for i in range(1, len(F)):
    F[i] = F[i - 1] * i % (10 ** 9 + 7)

# print(F[:100])
for i in range(k - 1, n):
    # print(i, k - 1, 123, permutations_count(i, k - 1))
    ans += a[i] * permutations_count(i, k - 1)

for i in range(n - k + 1):
    # print(n - i - 1, k - 1)
    ans -= a[i] * permutations_count(n - i - 1, k - 1)
print(ans % (10 ** 9 + 7))