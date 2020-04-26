import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
a, b, c, d = map(int, input().split())
a -= 1
cnt0B = b // c + b // d - b // lcm(c, d)
cnt0A = a // c + a // d - a // lcm(c, d)

print(b - a - (cnt0B - cnt0A))