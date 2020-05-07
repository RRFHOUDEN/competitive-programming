l, r = map(int, input().split())
ans = 10**10
for i in range(l, r+1):
    for j in range(i+1, r+1):
        ans = min(ans, (i*j)%(2019))
        if i*j%2019==0:
            break
    if i*j%2019==0:
        break
print(ans)