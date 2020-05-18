import math
ans = 0
p = [6/25, 6/25, 4/25, 4/25, 3/25, 2/25]
l = [1, 2, 3, 4, 5, 5]
for i in p:
    ans += math.log2(i) * i * (-1)
# for i in range(6):
#     ans += l[i] * p[i]

print(ans)