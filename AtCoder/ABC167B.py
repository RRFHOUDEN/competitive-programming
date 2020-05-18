a, b, c, k = map(int, input().split())

ans = 0
ans += 1 * min(a, k)
k -= a

if k > 0:
    ans += 0 * min(b, k)
    k -= b

if k > 0:
    ans += -1 * min(c, k)

print(ans)