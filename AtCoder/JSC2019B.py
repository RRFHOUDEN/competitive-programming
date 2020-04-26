n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
key = k
for i in range(n):
    for j in range(n):
        if a[i] > a[j] and i != j:
            if i < j:
                ans += (1 + key) * key // 2 % (10 ** 9 + 7)
            else:
                ans += (1 + key - 1) * (key - 1) // 2 % (10 ** 9 + 7)
        # print(ans, i, j)
ans %= ( 10 ** 9 + 7)
print(ans)