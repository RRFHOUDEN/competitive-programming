T = int(input())
for i in range(T):
    s = input()
    j = 4
    cnt = 0
    while j < len(s):
        if s[j - 4:j + 1] == "tokyo" or s[j - 4:j + 1] == "kyoto":
            cnt += 1
            j += 5
        else:
            j += 1
    print(cnt)