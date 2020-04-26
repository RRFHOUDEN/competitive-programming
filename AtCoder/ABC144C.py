import math
n = int(input())
ans = 10 ** 20

for i in range(int(math.sqrt(n) + 1), 0, -1):
    if n % i == 0:
        ans = min(ans, i - 1 + (n // i - 1))

print(ans)
