while True:
    input_data = input()
    if input_data == "#":
        break
    g, y, m, d = input_data.split()
    y = int(y)
    m = int(m)
    d = int(d)
    if y < 31 or (y == 31 and m <= 4):
        print(g, y, m, d)
    else:
        print("?", str(y - 30), str(m), str(d))