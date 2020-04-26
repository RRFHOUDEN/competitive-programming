import bisect
n = int(input())
s = input()
s_list = [[] for _ in range(10)]
for i in range(n):
    s_list[int(s[i])].append(i)
for i in range(10):
    s_list[i].sort()

can_use = [[0 for _ in range(10)] for _ in range(10)]

ans = 0
for i in range(1000):
    thisS = str(i)
    while len(thisS) < 3:
        # print(thisS)
        thisS = "0" + thisS

    if len(s_list[int(thisS[0])]) == 0:
        continue
    now_point = s_list[int(thisS[0])][0]
    # print(thisS, now_point)
    tmp = 0
    for j in range(2):
        tmp = 0
        now = int(thisS[j])
        next = int(thisS[j + 1])
        for k in range(len(s_list[next])):
            if s_list[next][k] > now_point:
                now_point = s_list[next][k]
                tmp = 1
                break
        if tmp == 0:
            break
    ans += tmp

print(ans)