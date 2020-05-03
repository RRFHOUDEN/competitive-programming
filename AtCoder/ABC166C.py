a, b, n = map(int, input().split())
x = min(n, b)
while x % b == 0 and b != 1:
    x -= 1
if b == 1:
    print(0)
else:
    i = x
    print(a * x // b)