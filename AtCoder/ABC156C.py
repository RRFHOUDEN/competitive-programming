n = int(input())
x = list(map(int, input().split()))
ans = 10 ** 10
for i in range(1, 101):
    tmp = 0
    for j in x:
        tmp += abs(i - j) ** 2
    ans = min(tmp, ans)

print(ans)