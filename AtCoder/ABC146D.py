n = int(input())
colorU = [-1 for _ in range(n)]
colorD = [-1 for _ in range(n)]
colorU[0] = 0

ab = []
ans = [0 for _ in range(n - 1)]
n -= 1
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b, i])
ab.sort()
for i in range(n):
    # print(i)
    a = ab[i][0]
    b = ab[i][1]
    c = ab[i][2]

    a -= 1
    b -= 1
    # print(i)
    if colorD[a] == -1:
        if colorU[a] == 1:
            thiscolor = 2
        else:
            thiscolor = 1
    else:
        thiscolor = colorD[a] + 1
        if thiscolor == colorU[a]: #1本目以外
            thiscolor += 1

    colorU[b] = thiscolor
    colorD[a] = thiscolor
    ans[c] = thiscolor
    # print(i)
    # print(thiscolor, i)

print(max(ans))
for i in ans:
    print(i)

# i = 0
# j = 0
# lasta = 0
#
# for l in range(n):
#     a, b = map(int, input().split())
#     if a != lasta:
#         i = a - 1
#         j = 0
#
#     if j == 0:
#         thiscolor = color[i] + 1
#     else:
#         thiscolor = graf[a][j - 1] + 1
#
#     graf[i].append()