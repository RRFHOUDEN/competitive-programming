X = int(input())
x = 100
for i in range(1000000):
    x = int(x * 1.01)
    if x >= X:
        print(i+1)
        break