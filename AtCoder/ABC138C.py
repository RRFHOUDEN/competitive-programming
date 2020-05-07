n = int(input())
v = list(map(int, input().split()))
v.sort()
tmp = v[0]
for i in range(1, n):
    tmp = tmp + v[i]
    tmp /= 2
print(tmp)