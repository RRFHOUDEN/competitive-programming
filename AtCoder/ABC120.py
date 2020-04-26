s = list(input())
cnt = 0
print(s)
acnt = 0
bccnt = 0

i = 0

while i < len(s):
    start = i
    end = i
    j = i

    if s[i] == "A":
        while j < len(s):
            if s[j] == "A":
                continue
            elif s[j:j + 2] == ["B", "C"]:
                end = j + 1
            elif s[j] == "C":
                break
            j += 1

        for j in range(i, end):
            if s[j] == "A":
                acnt += 1
            if s[j] == "B":
                bccnt += 1
    i = j + 1

print(cnt)