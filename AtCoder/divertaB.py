# n = int(input())
# xy = [list(map(int, input().split())) for _ in range(n)]
#
# sa = []
# for i, j in xy:
#     for k, l in xy:
#         sa.append([i - k, j - l])
#
# #sa1
# xy.sort()
# xy = xy[::-1]
# ans = 10000000000000000000
# i = 0
# while True:
#     if i >= len(sa):
#         break
#     if sa[i] == [0, 0]:
#         del sa[i]
#         i -= 1
#     i += 1
#
#
# if len(sa) == 0 and n != 1:
#     sa = [[1, 0], [0, 1]]
#
# for p, q in sa:
#     tmp = 1
#     for i in range(1, n):
#         a = xy[i][0]
#         b = xy[i][1]
#         if xy[i - 1][0] == a - p and xy[i - 1][1] == b - q:
#             1
#         else:
#             tmp += 1
#     ans = min(ans, tmp)
# xy.sort(key=lambda x:x[1])
# print(xy)
# for p, q in sa:
#     tmp = 1
#     for i in range(1, n):
#         a = xy[i][0]
#         b = xy[i][1]
#         if xy[i - 1][0] == a - p and xy[i - 1][1] == b - q:
#             1
#         else:
#             tmp += 1
#     print(tmp, p, q)
#     ans = min(ans, tmp)
# if n == 1:
#     ans = 1
# print(ans)

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy.sort()
sa = []
for i in range(n):
    for j in range(n):
        if i != j:
            sa.append([xy[i][0] - xy[j][0], xy[i][1] - xy[j][1]])

ans = 10 ** 15
for p, q in sa:
    tmp = 1
    for i in range(1, n):
        a = xy[i][0] - xy[i - 1][0]
        b = xy[i][1] - xy[i - 1][1]
        if p != a or q != b:
            tmp += 1
    ans = min(ans, tmp)

xy.sort(key=lambda x:x[1])
for p, q in sa:
    tmp = 1
    for i in range(1, n):
        a = xy[i][0] - xy[i - 1][0]
        b = xy[i][1] - xy[i - 1][1]
        if p != a or q != b:
            tmp += 1
    ans = min(ans, tmp)

if n == 1:
    ans = 1
print(ans)