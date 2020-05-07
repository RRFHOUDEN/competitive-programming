s = input()
begin = 1
tmp = ""
ans = []
for i in s:
    if begin and ord("A") <= ord(i) <= ord("Z"):
        tmp += i
        begin = 0
    elif not begin and ord("A") <= ord(i) <= ord("Z"):
        tmp += i
        begin = 1
        ans.append([tmp.lower(), tmp])
        tmp = ""
    else:
        tmp += i

ans.sort()
for _, i in ans:
    print(i, end ="")
print()