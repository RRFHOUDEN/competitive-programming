T = int(input())
anslist = []

for i in range(T):
    R, C = map(int, input().split())
    data = [list(input()) for i in range(R)]
    #print(data)
    onelist = []
    for j in range(len(data)):
        J = data[j]
        for k in range(len(J)):
            K = J[k]
            if K == "1":
                onelist.append([j, k])
    #print(onelist)
    disdata = [[0 for j in range(C)] for k in range(R)]
    for j in range(len(data)):
        for k in range(len(data[j])):
            if data[j][k] == "1":
                disdata[j][k] = 0
            else:
                thisdis = 10 ** 30
                for l, m in onelist:
                    thisdis = min(thisdis, abs(l - j) + abs(m - k))
                disdata[j][k] = thisdis

    ans = 10 ** 40
    import copy
    for j in range(len(data)):
        for k in range(len(data[j])):
            maxdis = 0
            thisdisdata = copy.deepcopy(disdata)
            thisdis = 10 ** 30
            for l, m in onelist:
                thisdis = min(thisdis, abs(l - j) + abs(m - k))
            ans = min(ans, maxdis)
    #print(disdata)
    #print(ans)
    anslist.append(ans)


for i in range(len(anslist)):
    print("Case #" + str(i + 1) + ": " + str(anslist[i]), end = "")
    if i + 1 != len(anslist):
        print()
