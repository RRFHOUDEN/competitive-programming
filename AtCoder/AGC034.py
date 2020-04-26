s = list(input())
def change(i):
    global s
    #print(i)
    if s[i : i + 3] == ["A", "B", "C"]:
        s[i:i + 3] = ["B", "C", "A"]
        #print(s)
        return 1
    return 0

cnt = 0
cnA = 0
i = 0
while i < len(s) - 1:
    #print(i, cnA)
    if s[i:i + 2] == ["B", "C"]:
        cnt += cnA
        i += 1
    elif s[i] == "A":
        cnA += 1
    else:
        cnA = 0
    i += 1

print(cnt)