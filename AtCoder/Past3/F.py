n = int(input())
s = [list(input()) for _ in range(n)]
res = ["" for _ in range(n)]
flag = 1
for i in range(n//2):
    alph = set(s[i])
    flag = 1
    for j in s[n-i-1]:
        if j in alph:
            res[i] = j
            res[n-i-1] = j
            flag = 0
            break
    if flag:
        break
if n == 1:
    flag = 0

if n % 2 != 0:
    res[n//2] = s[n//2][0]

if flag:
    print(-1)
else:
    for i in res:
        print(i, end="")
    print()