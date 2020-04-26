n = int(input())
a = list(map(int, input().split()))
guusuu = []
kisuu = []
for i in range(n):
    if i % 2 == 0:
        guusuu.append(a[i])
    else:
        kisuu.append(a[i])
key = n // 2

for i in range(1, n):
    if i < len(guusuu):
        guusuu[i] += guusuu[i - 1]
    if i < len(kisuu):
        kisuu[i] += kisuu[i - 1]

if 1:
    ans = -10 ** 10
    if n % 2 == 0:
        ans = kisuu[-1]
    for i in range(key):
        # print(i, ans)
        tmp = guusuu[i]
        tmp += kisuu[-1] - kisuu[i]
        ans = max(tmp, ans)
        print(i, tmp, ans, kisuu[-1], kisuu[i], guusuu[i])

    for i in range(key):
        print(i)
        tmp = kisuu[i]
        tmp += guusuu[-1] - guusuu[i + 1]
        ans = max(tmp, ans)
        print(i, tmp, ans, kisuu[-1], kisuu[i], guusuu[i])

    if n % 2 != 0:
        ans = max(ans, guusuu[-2], guusuu[-1] - guusuu[0])
print(ans, kisuu, guusuu)