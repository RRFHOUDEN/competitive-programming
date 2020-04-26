N = int(input())
group = []

ansanslist = [[0 for i in range(N)] for j in range(N)]
if N % 2 != 0:
    group.append([N])
N -= 1

for i in range(N // 2):
    group.append([i + 1, N - i])

anslist = []

for i in range(len(group)):
    for k in group[i]:
        for j in range(len(group)):
            for l in group[j]:
                if i != j:
                    anslist.append([k, l])

anslist.sort()
ansanslist = []
for i, j in anslist:
    if i < j:
        ansanslist.append([i, j])
print(len(ansanslist))
for i, j in ansanslist:
    print(i, j)
