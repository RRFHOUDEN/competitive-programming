n, m = map(int, input().split())
sc = [list(map(int, input().split())) for i in range(m)]
ans = -1
for i in range(10 ** (n - 1), 10 ** n):
    strI = str(i)
    ans = strI
    for s, c in sc:
        if strI[s - 1] != str(c):
            ans = -1
            break
    if ans != -1:
        break
if n == 1:
    for i in range(0, 10 ** n):
        strI = str(i)
        ans = strI
        for s, c in sc:
            if strI[s - 1] != str(c):
                ans = -1
                break
        if ans != -1:
            break
print(ans)