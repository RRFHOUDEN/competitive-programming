n = int(input())
a = list(map(int, input().split()))

x = []
tmp = 0
for i in range(n):
    if i % 2 == 0:
        tmp += a[i]
    else:
        tmp -= a[i]
x.append(tmp//2)

for i in range(n-1):
    x.append(a[i] - x[i])
# print(x)
for i in range(n):
    print(x[i]*2, end=" ")