m = int(input())
for i in range(m):
    s = list(input())
    kouho = []
    for i in range(1, len(s)):
        this1 = s[:i]
        this2 = s[i:]
        kouho.append([this1 + this2])
        kouho.append([this1[::-1] + this2])
        kouho.append([this1[::-1] + this2[::-1]])
        kouho.append([this1 + this2[::-1]])
        kouho.append([this2 + this1])
        kouho.append([this2[::-1] + this1])
        kouho.append([this2[::-1] + this1[::-1]])
        kouho.append([this2 + this1[::-1]])
    kouho.sort()
    #print(len(kouho))
    cnt = 0
    i = 1
    while i < len(kouho):
        if kouho[i] == kouho[i - 1]:
            del kouho[i]
            i -= 1
        i += 1
    print(len(kouho))