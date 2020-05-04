def solve():
    n, a, b, c = map(int, input().split())
    s = [input() for _ in range(n)]
    out = [[0, 0, 0] for _ in range(n)]
    tmp = [[0, 0, 0] for _ in range(n)]

    if s[0] == "AB":
        out[0] = [-1, 1, 0]
    elif s[0] == "BC":
        out[0] = [0, -1, 1]
    elif s[0] == "AC":
        out[0] = [-1, 0, 1]

    for i in range(n):
        if s[i] == "AB":
            tmp[i] = [1, 1, 0]
        if s[i] == "BC":
            tmp[i] = [0, 1, 1]
        if s[i] == "AC":
            tmp[i] = [1, 0, 1]

    for i in range(1, n):
        for j in range(3):
            out[i][j] = out[i-1][j] * tmp[i][j] * -1

        for j in range(3):
            if sum(out[i]) != 0 and tmp[i][j] != 0 and out[i][j] == 0:
                out[i][j] = -(sum(out[i]))
                break

    original = [a, b, c]
    check = 0
    for i in out:
        a += i[0]
        b += i[1]
        c += i[2]
        if not (0 <= a and 0 <= b and 0 <= c):
            check = 1

    if 0 <= a and 0 <= b and 0 <= c and not check:
        print("Yes")
        for i in out:
            for j in range(3):
                if i[j] == 1:
                    print(chr(ord("A") + j))
        return

    [a, b, c] = original
    check = 0
    for i in out:
        a -= i[0]
        b -= i[1]
        c -= i[2]
        if not (0 <= a and 0 <= b and 0 <= c):
            check = 1

    if 0 <= a and 0 <= b and 0 <= c and not check:
        print("Yes")
        for i in out:
            for j in range(3):
                if i[j] == -1:
                    print(chr(ord("A") + j))
        return
    print("No")

solve()