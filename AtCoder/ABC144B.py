n = int(input())
ans = -1
for i in range(1, 10):
    if n % i == 0 and (n // i) <= 9:
        print("Yes")
        ans = 1
        break
if ans == -1:
    print("No")