T = int(input())
anslist = []
for j in range(T):
    N, P = map(int, input().split())
    student = list(map(int, input().split()))
    student.sort()
    member = []

    tmp = 0
    for i in range(P - 1):
        tmp += student[P - 1] - student[i]
    member.append([tmp, 0, P - 1])

    for i in range(P, N):
        tmp += (student[i] - student[i - 1]) * (P - 1)
        tmp -= student[i - 1] - student[i - P]
        member.append([tmp, i - P + 1, i])
       # print(member, i, N)

   # print(min(member))
    a, l, r = min(member)
    ans = 0
    for i in range(l, r):
        ans += student[r] - student[i]
    anslist.append(ans)
    #print(ans)

for i in range(len(anslist)):
    print("Case #" + str(i + 1) + ": " + str(anslist[i]), end = "")
    if i + 1 != len(anslist):
        print()