# import fractions
# def lcm(x, y):
#     if x % y == 0:
#         return x
#     return (x * y) // fractions.gcd(x, y)


def gcd(a, b):
    if a % b == 0:
        return(b)

    else:
        return(gcd(b, a % b))


def lcm(a, b):
    return a / gcd(a, b) * b

n = int(input())
a = list(map(int, input().split()))
a.sort()
LCM = 1
for i in a[::-1]:
    LCM = lcm(LCM, i)
ans = 0
for i in a:
    tmp = LCM // i
    ans += tmp
    ans %= 10 ** 9 + 7
print(int(ans))
