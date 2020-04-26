t = int(input())
ans_list = []
def sarch(graf, now):
    for i in graf:
        if i == now:
            return False
    return True

for i in range(t):
    N, R, C, SR, SC = map(int, input().split())
    S = list(input())
    #print(S)
    graf = [[] for k in range(R)]
    now1 = SR - 1
    now2 = SC - 1
    graf[now1].append(now2)
    for j in S:
        #print(j)
        #print(now1, now2)
        if j == "N":
            while not sarch(graf[now1], now2):
                now1 -= 1
            graf[now1].append(now2)
        elif j == "S":
            while not sarch(graf[now1], now2):
                now1 += 1
            graf[now1].append(now2)
        elif j == "E":
            while not sarch(graf[now1], now2):
                now2 += 1
            graf[now1].append(now2)
        elif j == "W":
            while not sarch(graf[now1], now2):
                now2 -= 1
            graf[now1].append(now2)
        #print(j, now1, now2, graf)
    ans_list.append([now1 + 1, now2 + 1])
    #print(graf)

for i in range(len(ans_list)):
    print("Case #" + str(i + 1) + ":", str(ans_list[i][0]), str(ans_list[i][1]))