n, k = map(int, input().split())
for i in range(k, n+2):
    mini = (1+i)*i // 2
    maxi = (n+1-i)