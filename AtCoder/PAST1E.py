n, q = map(int, input().split())
follow = [[0 for _ in range(n)] for _ in range(n)]
for i in range(q):
    s = list(input().split())
    if len(s) == 3:
        follow[int(s[1])-1][int(s[2])-1] = 1
    else:
        if s[0] == "2":
            for j in range(n):
                if follow[j][int(s[1])-1]:
                    follow[int(s[1])-1][j] = 1

        else:
            check = []
            for j in range(n):
                if follow[int(s[1])-1][j]:
                    check.append(j)
            for j in check:
                for k in range(n):
                    if follow[j][k]:
                        follow[int(s[1])-1][k] = 1
                    # print(follow)


for i in range(n):
    for j in range(n):
        if i == j:
            print("N", end="")
        else:
            if follow[i][j]:
                print("Y", end="")
            else:
                print("N", end="")
    print()
