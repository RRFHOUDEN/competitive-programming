import math
k = int(input())
ans = 0
for i in range(1, k + 1):
    for j in range(i + 1, k + 1):
        for l in range(j + 1, k + 1):
            # print(i, j, l)
            ans += (math.gcd(math.gcd(i, j), l)) * 6

for i in range(1, k + 1):
    for j in range(i + 1, k + 1):
        # print(i, j)
        ans += math.gcd(i, j) * 6

for i in range(1, k + 1):
    # print(i)
    ans += i
print(ans)