n, d = map(int, input().split())
cnt = 1
now = d
while now+d+1 < n:
    cnt += 1
    now += 2*d+1
print(cnt)