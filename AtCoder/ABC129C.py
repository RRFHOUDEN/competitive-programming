n, m = map(int, input().split())
a = [0 for _ in range(n + 1)]
for i in range(m):
    A = int(input())
    a[A] = 1

tmp = [0 for _ in range(n + 1)]
tmp[0] = 1

for i in range(1, n + 1):
    if a[i] == 1:
        tmp[i] = 0
    else:
        if i - 2 >= 0:
            tmp[i] += tmp[i - 2]
        if i - 1 >= 0:
            tmp[i] += tmp[i - 1]
        tmp[i] %= 1000000007

print(tmp[n] % 1000000007)