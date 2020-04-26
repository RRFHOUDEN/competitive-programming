n, k = map(int, input().split())
ans = 0
cnt = 0
while n > 0:
    cnt += 1
    ans *= 10
    ans += n % k
    n //= k
print(cnt)