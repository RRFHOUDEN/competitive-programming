n, k = map(int, input().split())
v = list(map(int, input().split()))
import copy
originalV = copy.deepcopy(v)
ans = 0
#右端から採っていくのを全部試す+
for i in range(k):
    v = copy.deepcopy(originalV)
    j = 0
    tmp = 0
    thisk = k
    cnt = 0
    while len(v) > 0 and cnt < i:
        tmp += max(0, v[0])
        if v[0] < 0:
            cnt += 1
            thisk -= 1
        thisk -= 1
        cnt += 1
        del v[0]

    v = v[::-1]
    j = 0
    print(v, tmp, k - cnt)
    while len(v) > 0 and j < k - cnt:
        print(v[0])
        tmp += max(0, v[0])
        if v[0] < 0:
            thisk -= 1
            j += 1
        thisk -= 1
        del v[0]
        j += 1
    print(tmp)
    ans = max(ans, tmp)
print(ans)

6 1
-10 8 2 1 2 6