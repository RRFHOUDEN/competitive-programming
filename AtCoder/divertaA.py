n, k = map(int, input().split())
a = 1
b = 1 + (n - k)
if k == 1:
    print(0)
else:
    print(b - a)