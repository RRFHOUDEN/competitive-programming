def reorderLogFiles(logs):
    check = [0 for i in range(len(logs))]
    cnt = 0
    for i in logs:
        i = list(i.split())
        if "0" <= str(i[1][0]) <= "9":
            check[cnt] = 1
        else:
            check[cnt] = 0
        cnt += 1
    ansletter = []
    ansdigit = []
    for i in range(len(logs)):
        if check[i] == 0:
            tmp = list(logs[i].split())
            ansletter.append([tmp[1::], [tmp[0]]])

    ansletter.sort()
    # print(ansletter)

    ansletter2 = []
    for i in ansletter:
        tmp = i[-1] + i[0]
        ansletter2.append(" ".join(tmp))
    # print(ansletter2)

    for i in range(len(logs)):
        if check[i] == 1:
            ansdigit.append(logs[i])

    return ansletter2 + ansdigit


logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(reorderLogFiles(logs))

