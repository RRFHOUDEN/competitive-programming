anslist = []
T = int(input())
for k in range(T):
    n = int(input())
    sel = []
    max_time = 0
    zeroE = []
    for j in range(n):
        s, e, l = map(int, input().split())

        if l == 0:
            zeroE.append(e)
        else:
            sel.append([s, e, l])
    n = len(sel)
    dp = [[] for i in range(n)]

    while len(sel) != 0:
        key = 1
        for i in range(n):
            #print(sel[i][1])
            dp[i].append(sel[i][1])
            sel[i][1] -= sel[i][2] * sel[i][0]
            if sel[i][1] > 0:
                key = 0
            else:
                sel[i][1] = 0
        if key:
            break

    print(dp)

    ans = 0
    if len(sel) != 0:
        for i in range(min(n, len(dp[0])) - 1, -1, -1):
            # print(i)
            tmp = []
            thismax = 0
            for j in range(n):
                # print(j, i, n, len(dp[0]), dp[j][i])
                thismax = max(thismax, dp[j][i])

            for j in range(n):
                if dp[j][i] == thismax:
                    # print(j, i, 100)
                    tmp.append([sel[j][2], j])
            # print(dp)
            tmp.sort()
            #print(tmp)
            ans += thismax
            dp[tmp[0][1]] = [0 for j in range(len(dp[0]))]
            # print(ans)


    for i in zeroE:
        ans += i
    anslist.append(ans)
    #print(dp)

for i in range(len(anslist)):
    print("Case #" + str(i + 1) + ": " + str(anslist[i]))