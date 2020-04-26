n = int(input())
dic = {}
for i in range(n):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

cnt = 0
for i, j in dic.items():
    cnt = max(cnt, j)
ans = []
for i, j in dic.items():
    if cnt == j:
        ans.append(i)
ans.sort()
for i in ans:
    print(i)