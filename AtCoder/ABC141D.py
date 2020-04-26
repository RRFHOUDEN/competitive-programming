n, m  = map(int, input().split())
a = list(map(int, input().split()))

i = 0
if n == 1:
    while m > 0:
        a[0] //= 2
        m -= 1
else:
    while m > 0:
        # print(123)
        while a[i] >= a[i + 1] and m > 0:
            a[i] //= 2
            m -= 1
        while a[i] < a[i + 1]:
            # print(i)
            a[i], a[i + 1] = a[i + 1], a[i]
            i += 1
            if i == n - 1:
                break
        i = 0
        # print(a)

# print(a)
print(sum(a))

# import math
# import copy
# loga = copy.deepcopy(a)
# for i in range(n):
#     loga[i] = int(math.log2(a[i]))
#
# print(loga)
# loga.sort()
# loga = loga[::-1]
# print(loga)
# loga[0] -= (min(loga[0] - loga[1], m))
# m -= min(loga[0] - loga[1], m)
# print(loga, m)




# a.sort()
# a = a[::-1]
#
# i = 0
# while m > 0:
#     if i < n - 1:
#         while a[i] >= a[i - 1] and a[i] >= a[i + 1] and m > 0:
#             a[i] //= 2
#             m -= 1
#         if a[i - 1] > a[i + 1]:
#             i -= 1
#         else:
#             i += 1
#     else:
#         while a[i] >= a[i - 1] and m > 0:
#             a[i] //= 2
#             m -= 1
#         i -= 1
#
# print(sum(a))