n, k = map(int, input().split())
cnt = 0
for i in range(k, n+2):
    mini = (i-1) * i // 2
    maxi = (n+n-i+1) * i // 2
    # print(i, mini, maxi)
    cnt += maxi - mini + 1
    cnt %= 10 ** 9 + 7
print(cnt)