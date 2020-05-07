n = int(input())
a = [int(input()) for _ in range(n)]

for i in range(1, n):
    if a[i-1] < a[i]:
        print("up", a[i] - a[i-1])
    elif a[i-1] == a[i]:
        print("stay")
    else:
        print("down", a[i-1] - a[i])