n = int(input())
s = input()
newS = []
for i in s:
    new = chr(ord(i) + n)
    if new > "Z":
        new = chr(ord(i) + n - 26)
    newS.append(new)

for i in newS:
    print(i, end = "")
print()