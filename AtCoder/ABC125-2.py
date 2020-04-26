n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
key = 0
ans = 0
for i in range(1, n):
    tmp1 = ab[ans][0] // ab[i][1]
    if ab[ans][0] % ab[i][1] != 0:
        tmp1 += 1
    tmp2 = ab[i][0] // ab[ans][1]
    if ab[i][0] % ab[ans][1] != 0:
        tmp2 += 1

    if tmp1 < tmp2:
        ans = i

for i in range(n):
    if i != ans:
        if (ab[ans][0] + ab[i][1] - 1) / ab[i][1] < (ab[i][0] + ab[ans][1] - 1) / ab[ans][1]:
            print(i)
            key = 1
    if key:
        break

if key:
    print(-1)
else:
    print(ans + 1)