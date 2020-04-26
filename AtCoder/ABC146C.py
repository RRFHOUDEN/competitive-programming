a, b, x = map(int, input().split())
ans = 0
aasdf = []
for i in range(10, 0, -1):
    thisX = x
    thisX -= b * i
    n = thisX // a
    # print(thisX, i, n)
    if len(str(n)) == i and n >= 0:
        ans = n
        break
    elif len(str(n)) > i and n >= 0:
        ans = min(10 ** (i) - 1, n)
        break

print(min(ans, 10 ** 9))
# 1000000000 1000000000 1000000000000000000