S, T = input().split()
a, b = map(int, input().split())
u = input()
if S == u:
    print(a - 1, b)
else:
    print(a, b - 1)