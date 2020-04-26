s = input()
k = int(input())
cnt = 0
i = 0
c0 = 0
c1 = 0
key = 0
endkey = 0
while i < len(s) - 1:
    if s[i] == s[i + 1]:
        start = i
        end = i
        for j in range(i + 1, len(s)):
            end = j
            if s[j] != s[i]:
                break

        if end == len(s) - 1: #もし最後の一文字が連続に含まれるとき
            if (end - start) % 2 == 0 and s[-1] == s[0]: #最後の一文字が連続でかつ最初の文字と同じでかつ奇数の時
                end += 1
                endkey = 1
            elif s[-1] == s[0]:
                endkey = 2
            end += 1

        if start == 0 and end == len(s) + 1 and len(s) % 2 == 1:
            key = 1
            cnt += (end - start - 1) * (k // 2)
            if k % 2 == 1:
                cnt += (end - start - 1) // 2
        else:
            cnt += (end - start) // 2 * k
        i = end - 1
    i += 1
if len(s) == 1:
    cnt += k // 2
elif not endkey and not key and s[0] == s[-1]:
    cnt += k - 1
if endkey == 1 and not key:
    cnt -= 1
print(cnt)