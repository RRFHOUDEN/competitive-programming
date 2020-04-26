while True:
    n, m, t, p = map(int, input().split())
    if n == 0 and m == 0 and t == 0 and p == 0:
        break
    paper = [[1 for i in range(n)] for j in range(m)]
    print(paper)
    for i in range(t):
        d, c = map(int, input().split())
        if d == 1:
            for k in range(len(paper)):
                for j in range(c, min(2 * c, len(paper[0]))):
                    paper[k][j] += paper[k][j - c]
                    print(k, j)
                del paper[k][:c]
        elif d == 2:
            for k in range(len(paper[0])):
                for j in range(c, min(2 * c, len(paper))):
                    paper[j][k] += paper[j - c][k]
            del paper[:c]
        print(paper)
    for i in range(p):
        x, y = map(int, input().split())
        print(paper[y][x])