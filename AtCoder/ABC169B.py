n = int(input())
a = list(map(int, input().split()))

res = 1
if min(a) == 0:
    res = 0
for i in a:
    res *= i
    if res > 10 ** 18:
        res = -1
        break

print(res)