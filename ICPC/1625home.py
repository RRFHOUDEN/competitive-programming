while True:
    n, m, t, p = map(int, input().split())
    origami = [[0 for _ in range(10 * n)] for _ in range(10 * m)]
    for i in range(m):
        origami[i][:n] = [1 for _ in range(n)]

    for i in range(t):
        d, c = map(int, input().split())
        k = 0

        if d == 1:
            for j in range(c):
                for k in range(len(origami)):
                    origami[k][c + j] += origami[k][c - j - 1]
                    origami[k][c - j - 1] = 0
            for j in range(len(origami)):
                while k < len(origami[j]):
                    if origami[j][k] == 0:
                        del origami[j][k]
                        k -= 1
                    elif origami[j][k] != 0:
                        break
                    k += 1
        else:
            for j in range(c):
                for k in range(min(len(origami[c + j]), len(origami[c - j - 1]))):
                    origami[c + j][k] += origami[c - j - 1][k]
            for j in range(len(origami)):
                while k < len(origami[j]):
                    if origami[j][k] == 0:
                        del origami[j][k]
                        k -= 1
                    elif origami[j][k] != 0:
                        break
                    k += 1
        
    print(origami)
    for i in range(p):
        x, y = map(int, input().split())
        print(origami[x][y])