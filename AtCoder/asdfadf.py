s = list(input())
cnt = 0
for i in range(len(s) - 2):
    if s[i:i + 3] == ["A", "B", "C"]:
        s[i:i + 3] = ["B", "C", "A"]
        cnt += 1
    #print(i)

for i in range(len(s) - 1, 1, -1):
    if s[i - 2:i + 1] == ["A", "B", "C"]:
        s[i - 2:i + 1] = ["B", "C", "A"]
        cnt += 1
    #print(i)

print(cnt, s)
