m, d = map(int, input().split())
ans = 0
for i in range(1, m + 1):
    for j in range(min(22, d), d + 1):
        if j // 10 * (j % 10) == i and j % 10 > 1:
            # print(j// 10, j % 10, i)
            ans += 1
print(ans)