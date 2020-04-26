N, K = map(int, input().split())
s = list(input())

cnt = 1
cntlist = []
for i in range(1, N):
    if s[i - 1] != s[i]:
        cntlist.append(cnt)
        cnt = 1
    else:
        cnt += 1

cntlist.append(cnt)
if s[0] == "0":
    cntlist = [0] + cntlist

ans = 0
for i in range(2 * K + 1):
    if i >= len(cntlist):
        break
    ans += cntlist[i]
anslist = [ans]
s = 0
g = 2 * K + 1
while g < len(cntlist):
    ans -= cntlist[s]
    ans -= cntlist[s + 1]
    s += 2
    ans += cntlist[g]
    g += 1
    if g >= len(cntlist):
        anslist.append(ans)
        break
    ans += cntlist[g]
    g += 1
    anslist.append(ans)

print(max(anslist))