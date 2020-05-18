s = input()
n = len(s)

rl = []
for i in range(n-1):
    if s[i] != s[i+1] and s[i] == "R":
        rl.append(i)

even = rl[0] + 1
odd = rl[0]
next = 1
ans = [0 for _ in range(n)]

for i in range(n):
    if 0 < i and s[i] == "R" and s[i-1] == "L":
        even = rl[next] + 1
        odd = rl[next]
        next += 1

    if (i % 2 == 0 and even % 2 == 0) or (i % 2 != 0 and even % 2 != 0):
        ans[even] += 1
    else:
        ans[odd] += 1

for i in ans:
    print(i, end=" ")