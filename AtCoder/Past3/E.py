n, m, q = map(int, input().split())
graf = [[] for _ in range(n)]
for i in range(m):
    v1, v2 = map(int, input().split())
    graf[v1-1].append(v2-1)
    graf[v2-1].append(v1-1)

c = list(map(int, input().split()))

for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        print(c[s[1]-1])
        for j in graf[s[1]-1]:
            c[j] = c[s[1]-1]
    else:
        print(c[s[1]-1])
        c[s[1]-1] = s[2]