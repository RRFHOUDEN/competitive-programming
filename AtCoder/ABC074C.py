a, b, c, d, e, f = map(int, input().split())

water = [0 for _ in range(f+1)]
sugure = [0 for _ in range(f+1)]
i = 0
while 100 * a * i <= f:
    j = 0
    while 100 * a * i + 100 * b * j <= f:
        water[100 * a * i + 100 * b * j] = 1
        j += 1
    i += 1
i = 0
while c * i <= f:
    j = 0
    while c * i + d * j <= f:
        sugure[c * i + d * j] = 1
        j += 1
    i += 1

ans = []
for i in range(1, f+1):
    if water[i]:
        j = 0
        tmp = 0
        i_ans = [0, 0, 0]
        while 100 * j / (i + j) <= e * 100 / (100 + e) and j <= f and i + j <= f:
            if sugure[j]:
                i_ans = [100 * j / (i + j), i, j]
            j += 1
        ans.append(i_ans)
ans.sort(reverse=True)
ans = ans[0]
print(ans[1]+ans[2], ans[2])