x = int(input())
check = 0
for a in range(1000):
    for b in range(-1000, 1000):
        if a ** 5 - b ** 5 == x:
            print(a, b)
            check = 1
            break
    if check:
        break
