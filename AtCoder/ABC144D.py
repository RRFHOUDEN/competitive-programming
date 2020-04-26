import math
a, b, x = map(int, input().split())
PI = 3.1415926535897932384626
if x >= a * a * b / 2:
    ans = math.atan(2 * (a * a * b - x) / (a * a * a))
    ans = math.degrees(ans)
else:
    ans = math.atan(2 * x / (a * b * b))
    ans = math.degrees(ans)
    ans = 90 - ans
print(ans)