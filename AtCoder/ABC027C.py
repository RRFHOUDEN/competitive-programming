n = int(input())

x = 1
turn = 0
while x <= n:
    if turn == 1:
        x *= 2
        turn = 0
    else:
        x *= 2
        x += 1
        turn = 17
print(x, turn)
print("Aoki")