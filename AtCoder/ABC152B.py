a, b = map(int, input().split())
A = 0
for i in range(b):
    A += a * 10 ** (i)
B = 0
for i in range(a):
    B += b * 10 ** (i)

if a < b:
    print(A)
else:
    print(B)