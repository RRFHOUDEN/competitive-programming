import math
a, b, h, m = map(int, input().split())

long = 360 * h / 12 + 360 / 12 * m / 60
short = 360 * m / 60
# long *= math.pi / 180
# short *= math.pi / 180
if True:
    theta = abs(long - short) * math.pi / 180
    B = a * math.cos(theta) - b
    A = a * math.sin(theta)
    print(math.sqrt(A*A + B*B))