def prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 1
    return 1

x = int(input())
while not prime(x):
    x += 1
    # print(x)
print(x)