n = int(input())
a = list(map(int, input().split()))
num = [0 for _ in range(n)]
c = [0 for _ in range(n)]
for i in a:
    num[i - 1] += 1

for i in range(n):
    if num[i] == 0:
        continue
    c[i] = num[i] * (num[i] - 1) // 2
# print(c)
ans = sum(c)
# print(num)
for i in a:
    tmp = (num[i - 1] - 2) * (num[i - 1] - 1) // 2 - num[i - 1] * (num[i - 1] - 1) // 2
    print(ans + tmp, )