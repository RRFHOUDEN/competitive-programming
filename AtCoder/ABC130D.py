n, k = map(int, input().split())
a = list(map(int, input().split()))
import copy
originalA = copy.deepcopy(a)
ans = 0
start = 0
# for i in range(1, n):
#     a[i] += a[i - 1]
#     key = 0
#     print(a)
#     if a[i] >= k:
#         key = 1
#         for j in range(start, i):
#             if a[i] - a[j] >= k:
#                 key += 1
#         a[i] = 0
#         start = i + 1
#     ans += key * (n - i)
#     print(i, a, key, ans)

for i in range(1, n):
    a[i] += a[i - 1]
a = [0] + a
# print(a)
for i in range(n + 1):
    # print(i, start, a[i] - a[start], ans)
    while a[i] - a[start] >= k:
        # print(i, start)
        ans += (n - i + 1)
        start += 1
        # print(12)



print(ans)