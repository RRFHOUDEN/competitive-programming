import fractions


x, y = map(int, input().split())
X = x
Y = y
ans = 0
while True:
    # print(x, y)
    if y == x * 2:
        ans = 1
        break
    elif x < 0 or y < 0:
        ans = 0
        break
    x -= 2
    y -= 1

def ANS(a, b):
    ans = 1
    j = b
    J = 1
    # print(a, b)
    for i in range(a, a - b, -1):
        ans *= i
        if ans % j == 0:
            ans //= J
            ans %= 10 ** 9 + 7
        else:
            J *= j
            ans %= 10 ** 9 + 7
            J %= 10 ** 9 + 7

        # print(ans)
        j -= 1
        # print(ans, i, j)
    return ans

# print(1, ans, x, y)
xx = 0
yy = 0
# print(x, y)
if ans == 0:
    print(ans)
else:
    xx = X - x
    xx //= 2
    yy = y // 2
    key = xx + yy;
    for i in range(1, yy + 1):
        ans *= key / i
        ans %= 10 ** 9 + 7
        key -= 1
    print(ans)