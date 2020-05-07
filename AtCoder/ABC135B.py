n = int(input())
p = list(map(int, input().split()))

check = 1
for i in range(n):
    if p[i] != i+1:
        check = 0
        if p[p[i]-1] == i+1:
            print("YES")
        else:
            print("NO")
        break

if check:
    print("YES")