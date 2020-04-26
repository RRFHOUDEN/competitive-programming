n = int(input())
a = list(map(int, input().split()))
key = n / 2
if key == n // 2:
    key -= 1
else:
    key = int(key)

ans = 0
for i in range(n):
    cnt = 0
    tmp = 0
    j = i
    while j < n and cnt < key:
        tmp = a[j]
        j += 2
        cnt += 1
    if cnt == key:
        ans = max(ans, tmp)
print(ans)