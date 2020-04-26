n, m = map(int, input().split())
# ps = [list(map(int, input().split())) for _ in range(m)]
ans = [0 for _ in range(n)]
pe = [0 for _ in range(n)]
accnt = 0
pecnt = 0
for i in range(m):
    p, s = input().split()
    p = int(p)
    if ans[p - 1] == 0 and s == "WA":
        pe[p - 1] += 1
    elif ans[p - 1] == 0 and s == "AC":
        ans[p - 1] = 1

for i in range(n):
    if ans[i] == 0:
        pe[i] = 0

print(sum(ans), end = " ")
print(sum(pe), end = "")
print()