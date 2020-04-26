n = int(input())
s = input()
abcList = [[] for i in range(n)]
for i in range(n):
    moji = s[i]
    abcList[ord(moji) - ord("a")].append(i)
print(abcList)
q = int(input())
for i in range(q):
    q, il, cr = map(int, input().split())
    if q == 1:
        i = il
        c = cr
        left = 0
        right = len(abcList)
        while left < right:
            mid = (left + right) // 2
            if abcList[mid] == -1:
                mid -= 1
            if left == mid:
                pass