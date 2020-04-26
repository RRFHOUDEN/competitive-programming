m = int(input())
dc = [0 for _ in range(m)]
ans = 0
for i in range(m):
    d, c = map(int, input().split())
    tmp = d * c
    if len(str(tmp)) == 2:
        tmp = (tmp // 10) + (tmp % 10)
        ans += 1

    dc[i] = tmp
    ans += c - 1

# print(dc, ans)
SUM = 0

m = len(dc)
for i in range(m):
    SUM += dc[i] * 10 ** (m - i - 1)

# print(SUM)
i = 0
while (i < m - 1):
    # print(i, ans, SUM)
    SUM -= (dc[i] * 10 + dc[i + 1]) * 10 ** ((m - i - 2))
    # print(SUM, 12121212)
    ans += 1
    tmp = dc[i] + dc[i + 1]
    # print(tmp, SUM, i)

    if len(str(tmp)) == 2:
        tmp = (tmp // 10) + (tmp % 10)
        ans += 1

    dc[i + 1] = tmp
    SUM += tmp * 10 ** ((m - i - 2))
    i += 1

    if SUM <= 9:
        break

print(ans)
