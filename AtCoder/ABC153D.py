import math
h = int(input())
# cnt = 0
# while h > 0:
#     if h == 1:
#         cnt += 1
#         break
#     else:
#         h //= 2
#         cnt += 1

ans = math.log2(h)
ans = int(ans)
#
# print(2 ** cnt - 1)
print(2 ** (int(ans) + 1) - 1)