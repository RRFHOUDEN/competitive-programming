anslist = []
while True:
    ans = 0
    n = int(input())
    if not n:
        break

    w = [len(input()) for i in range(n)]

    print(w)
    i = 0
    while True:
        #sarch 5
        while True:
            if cnt < 5:
                cnt += w[i]
            elif cnt > 5:
                i += 1
                break
            else:

    anslist.append(ans)

for i in anslist:
    print(i)