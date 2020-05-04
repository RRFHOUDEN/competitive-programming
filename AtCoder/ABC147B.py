s = input()
cnt = 0
for i in range(len(s)):
    j = len(s) - i - 1
    if j < i:
        break
    if s[i] != s[j]:
        cnt += 1
print(cnt)