import sys
sys.setrecursionlimit(1000000)

n, a, b = map(int, input().split())
mod = 10**9 + 7
nca = 1

for i in range(a):
    nca *= (n-i)
    nca *= pow(i+1, mod-2, mod)
    nca %= mod
ncb = 1
for i in range(b):
    ncb *= (n-i)
    ncb *= pow(i+1, mod-2, mod)
    ncb %= mod

nca %= mod
ncb %= mod


ans = pow(2, n, mod) - nca - ncb - 1
# print(pow(2, n, mod), nca, ncb)
while ans < 0:
    ans += mod
print(ans)