def sarch(l, left, right, target):
    global ans, cnt
    cnt += 1
    if cnt > 100000:
        return 0
    mid = right + left
    mid //= 2
    # print(left, right, target, ans)
    if right - left <= 1:
        if l[right] >= target:
            return right
        if l[left] >= target:
            return left
        else:
            return 0

    if target < l[mid]:
        # print(2)
        return sarch(l, mid, right, target)
    if target == l[mid]:
        return mid
    if l[mid] < target:
        # print(1)
        return sarch(l, left, mid, target)

cnt = 0
n = int(input())
l = list(map(int, input().split()))
l.sort()
l = l[::-1]
# print(l)
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        target = l[i] - l[j] + 1
        tmp = sarch(l, j + 1, n - 1, target)
        # print(tmp, j)
        if tmp > j:
            ans += (tmp - j)

print(ans)
