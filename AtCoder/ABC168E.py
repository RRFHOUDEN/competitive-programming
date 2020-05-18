n = int(input())
apb = {}
bpa = {}

cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    if a/b in bpa:
        cnt += bpa[a/b]

    if a/b in apb:
        apb[a/b] += 1
    else:
        apb[a/b] = 1

    if -b/a in bpa:
        bpa[-b/a] += 1
    else:
        bpa[-b/a] = 1

print(apb, bpa, cnt)