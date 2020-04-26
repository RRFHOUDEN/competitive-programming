n = int(input())
tmp = [[0 for i in range(9)] for j in range(9)]

for i in range(1, n + 1):
    strI = str(i)
    if strI[-1] == "0":
        continue
    tmp[int(strI[0]) -1 ][int(strI[-1]) - 1] += 1

ans = 0
for i in range(9):
    for j in range(9):
        ans += tmp[i][j] * tmp[j][i]

print(ans)