import bisect
INF = 10 ** 10
s = input()
t = input()
moji = [[] for _ in range(26)]

for i, m in enumerate(s):
    moji[ord(m) - ord("a")].append(i)

for i in range(26):
    moji[i].sort()

moji_o = [0 for _ in range(len(t))]

cnt = 0
ans = 1
# print(moji)
for i, m in enumerate(t):
    if len(moji[ord(m) - ord("a")]) == 0:
        ans = -1
        break
    if i == 0:
        moji_o[i] = moji[ord(m) - ord("a")][0]
    else:
        if moji_o[i - 1] >= moji[ord(m) - ord("a")][-1]:
            moji_o[i] =  moji[ord(m) - ord("a")][0]
        else:
            tmp = bisect.bisect_right(moji[ord(m) - ord("a")], moji_o[i - 1])
            if tmp == 0:
                moji_o[i] = moji[ord(m) - ord("a")][0]
            else:
                moji_o[i] = moji[ord(m) - ord("a")][tmp]
# print(moji_o)
for i in range(1, len(moji_o)):
    if ans == -1:
        break
    if moji_o[i - 1] >= moji_o[i]:
        cnt += 1

if ans == -1:
    print(-1)
else:
    print(cnt * len(s) + moji_o[-1] + 1)