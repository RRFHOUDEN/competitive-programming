n, m, k = map(int, input().split())
# tmp = m
mod = 998244353
ans = m * pow(m-1, n-1, mod)
ans %= mod
ncm = 1
ncm_list = [0 for _ in range(k)]
for i in range(k):
    ncm *= n-1-i
    ncm *= pow(i+1, mod-2, mod)
    ncm %= mod
    ncm_list[i] = ncm

powm_list = [0 for _ in range(k)]
tmp = m * pow(m-1, n-k-1, mod)
if k != 0:
    powm_list[k-1] = tmp
    for i in range(k-2, -1, -1):
        tmp *= (m-1)
        tmp %= mod
        powm_list[i] = tmp

for i in range(k):
    ans += ncm_list[i] * powm_list[i]
    ans %= mod

print(ans)