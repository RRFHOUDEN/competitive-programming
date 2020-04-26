a = [list(map(int, input().split())) for _ in range(3)]
A = [[0, 0, 0] for i in range(3)]
n = int(input())
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if a[j][k] == b:
                A[j][k] = 1

ans = 0
for i in range(3):
    if sum(A[i]) == 3:
        ans = 1

for i in range(3):
    s = 0
    for j in range(3):
        s += A[j][i]
    if s == 3:
        ans = 1

s = 0
for i in range(3):
    s += A[i][i]
if s == 3:
    ans = 1

s = 0
for i in range(3):
    s += A[i][2 - i]
if s == 3:
    ans = 1

if ans:
    print("Yes")
else:
    print("No")
