def check_sosu(n):
    if n < 2:
        return 0
    j = 2
    while j * j <= n:
        if n % j == 0:
            return 0
        j += 1
    return 1

# k = int(input())
# print(check_sosu(k))
for i in range(10**6+10, 10**7):
    if check_sosu(i):
        print(i)
        break