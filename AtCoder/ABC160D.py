n, x, y = map(int, input().split())
graf = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        graf[i][j] = graf[i][j - 1] + 1

# (y - x - 1)
# for i in range(x):
#     for j in range(y - 1, n):
#         graf[i][j] -= y - x - 1
#
#     for j in range(y - 2, x - 1, -1):
#         graf[i][j] = min(graf[i][j], graf[i][j + 1] + 1)

for i in range(n):
    for j in range(i + 1, n):
        graf[i][j] = min(graf[i][j], abs(i - x + 1) + abs(y - 1 - j) + 1)

# print(graf)
k = [0 for _ in range(n)]
for i in graf:
    for j in i:
        k[j] += 1
# print(k)
for i in k[1::]:
    print(i)