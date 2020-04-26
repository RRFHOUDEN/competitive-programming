n = int(input())
a = list(map(int, input().split()))
a.sort()
anslist = []
for i in range(1, n - 1):
    if a[i] >= 0:
        anslist.append([a[0], a[i]])
        a[0] -= a[i]
    else:
        anslist.append([a[-1], a[i]])
        a[-1] -= a[i]

anslist.append([a[-1], a[0]])
ans = a[-1] - a[0]
print(ans)
for i, j in anslist:
    print(i, j)
#
# a.sort()
# ans = a[0]
# for i in range(1, n - 1):
#     ans += a[i] * (-1)
#
# print(a[-1] - ans)
# key = a[0]
# for i in range(1, n - 1):
#     print(key, a[i])
#     key = key - a[i]
# print(a[-1], key)

# a.sort()
# plusa = []
# minusa = []
# for i in a[1:-1]:
#     if i < 0:
#         minusa.append(i)
#     else:
#         plusa.append(i)
# #
# # print(minusa, plusa)
# anslist = []
# # if len(a) == 2:
# #     print(max(a) - min(a))
# #     print(max(a), min(a))
# # if min(a) >= 0:
# #     for i in range(1, n - 1):
# #         anslist.append([a[0], a[i]])
# #         a[0] -= a[i]
# #     anslist.append([a[-1], a[0]])
# #     print(a[-1] - a[0])
# #     for i, j in anslist:
# #         print(i, j)
# # else:
# #     if len(plusa) == 0:
# #         plusa.append(minusa[-1])
# #         del minusa[-1]
# #
# #     for i in minusa:
# #         # print(plusa[0], i)
# #         anslist.append([plusa[0], i])
# #         plusa[0] -= i
# #
# #     for i in plusa:
# #         # print(a[0], i)
# #         anslist.append([a[0], i])
# #         a[0] -= i
# #     # print(a[0])
# #     print(a[-1] - a[0])
# #     for i, j in anslist:
# #         print(i, j)
# #     # print(anslist)
# #     print(a[-1], a[0])