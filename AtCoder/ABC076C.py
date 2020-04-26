s = input()
t = input()
cnt = 0
for i in range(len(s) - len(t), -1, -1):
    cnt = 0
    for j in range(len(t)):
        if s[j + i] == "?" or s[j + i] == t[j]:
            cnt += 1
        else:
            break
    if cnt == len(t):
        for j in range(len(s)):
            if i <= j < i + len(t):
                print(t[j - i], end = "")
            elif s[j] == "?":
                print("a", end = "")
            else:
                print(s[j], end = "")
        print()
        break
if cnt != len(t):
    print("UNRESTORABLE")