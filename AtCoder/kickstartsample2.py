T = int(input())
anslist = []

for i in range(T):
    l, r = map(int, input().split())
    cnt = 0
    for j in range(l, r + 1):
        check = 1
        if j % 9 != 0:
            for k in list(str(j)):
                if k == "9":
                    check = False
            if check:
                cnt += 1
    anslist.append(cnt)

for i in range(len(anslist)):
    print("Case #" + str(i + 1) + ": " + str(anslist[i]))



