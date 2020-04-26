n, k, q = map(int, input().split())
point = [0 for _ in range(n)]
for i in range(q):
    a = int(input())
    point[a - 1] += 1
# print(point)
for i in range(n):
    point[i] += k - q
    if point[i] > 0:
        print("Yes")
    else:
        print("No")