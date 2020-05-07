n = int(input())
a = list(map(int, input().split()))
onecnts = []

for i in a:
    j = 0
    while i > 0:
        if len(onecnts) - 1 < j:
            onecnts.append(0)
        if i % 2 != 0:
            onecnts[j] += 1
        j += 1
        i >>= 1

ans = 0
mod = 10**9+7

for i, onecnt in enumerate(onecnts):
    ans += onecnt * (n-onecnt) * (2**i)
    ans %= mod
print(ans)