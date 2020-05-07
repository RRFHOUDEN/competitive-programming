import fractions
a, b, x = map(int, input().split())
PI = 3.1415926535897932384626
if x >= a * a * b / 2:
    ans = fractions.atan(2 * (a * a * b - x) / (a * a * a))
    ans = fractions.degrees(ans)
else:
    ans = fractions.atan(2 * x / (a * b * b))
    ans = fractions.degrees(ans)
    ans = 90 - ans
print(ans)