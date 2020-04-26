n = int(input())
w = list(map(int, input().split()))
ans = 10000000000
for i in range(1, n):
    #print(i)
    tmp1 = 0
    tmp2 = 0
    for j in range(i):
        #print(j)
        tmp1 += w[j]
    for j in range(i, n):
        tmp2 += w[j]
    ans = min(abs(tmp2 - tmp1), ans)

print(ans)