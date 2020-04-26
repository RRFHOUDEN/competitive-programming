n = int(input())
graf1 = [[] for _ in range(n)]
graf2 = [[] for _ in range(n)]
graf3 = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    if b < a:
        a, b = b, a
    graf2[a - 1].append(b - 1)
    graf1[b - 1].append(a - 1)
    graf3[a - 1].append(b - 1)
    graf3[b - 1].append(a - 1)

value = [[0, 0] for _ in range(n)]
# print(graf1, graf2)
for i, j in enumerate(graf1):
    if len(j) == 0:
        value[i][0] = 1
    else:
        for k, l in enumerate(j):
            value[i][0] += value[l][0]

for i, j in enumerate(graf2[::-1]):
    # print(j)
    if len(j) == 0:
        value[n - i - 1][1] = 1
    else:
        for k, l in enumerate(j):
            # print(i, j ,k, l, value[l][1])
            value[n - i - 1][1] += value[l][1]

print(graf1, graf2)
print(value)
ans = [1 for _ in range(n)]
# for i, j in enumerate(graf1):
#     for k in j:
#         ans[i] *= value[k][0]
# for i, j in enumerate(graf2):
#     for k in j:
#         ans[i] *= value[k][1]
for i, j in value:
    print(i * j)
print(ans)
