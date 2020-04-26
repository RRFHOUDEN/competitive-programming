anslist = []
T = int(input())
for k in range(T):
    n = int(input())
    sel = []
    max_time = 0
    for j in range(n):
        s, e, l = map(int, input().split())
        sel.append([s, e, l])
        if l != 0:
            max_time = max(e // l + 1,max_time)

    dp = [[[0, 0] for j in range(max_time)] for k in range(n)]

    thisE = sel[0][1]
    dp[0][0] = [thisE, thisE]
    for i in range(1, min(sel[0][1] // sel[0][2] + 1, max_time - sel[0][0])):
        dp[0][i] = [thisE, max(thisE, dp[0][i - 1][1])]
        thisE -= sel[0][2]
        if thisE < 0:
            break

    for i in range(1, n):
        for j in range(max_time):
            if j + 1 < sel[i][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j][0] = max(dp[i - 1][j - sel[i][0]][1] + max(sel[i][1] - (j - sel[i][0]) * sel[i][2], 0), dp[i - 1][j][1])
    print(dp)
    anslist.append(max(dp[n - 1]))
    print(dp)
for i in range(len(anslist)):
    print("Case #" + str(i + 1) + ": " + str(anslist[i]))