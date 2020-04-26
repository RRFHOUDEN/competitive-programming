n, k = map(int, input().split())
v = list(map(int, input().split()))
import copy
originalV = copy.deepcopy(v)
gyakuv = v[::-1]
ans = 0
for i in range(k + 1): #i個使う
    if i >= n:
        break
    this = []
    for j in range(i + 1): #右からj個使う左からi - j // n > iの時
        #print(i)
        this = v[:j] + gyakuv[:min(max(i - j, 0), n - j)]
        print(this, j, i)
        tmp = sum(this)
        this.sort()
        for asd in range(min(k - i, len(this))):
            if this[asd] >= 0:
                break
            tmp -= this[asd]

        ans = max(tmp, ans)


print(ans)