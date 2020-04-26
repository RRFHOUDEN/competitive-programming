n = int(input())
a = list(map(int, input().split()))
cnt = 1
for i in range(n):
    if a[i] == cnt:
        cnt += 1
cnt -= 1
ans = n - cnt
if cnt == 0:
    ans = -1
print(ans)