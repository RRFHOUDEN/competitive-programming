n = int(input())
a = list(map(int, input().split()))
tmp = 0
key = 0
SUMA = sum(a)

for i in range(n):
    if tmp + a[i] >= SUMA / 2:
        key = i
        break
    tmp += a[i]

ans = abs(sum(a[0:key]) - sum(a[key::]))
tmp = 0
key += 1
ans = min(abs(sum(a[0:key]) - sum(a[key::])), ans)
print(ans)
