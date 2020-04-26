import bisect
n = int(input())
S = input()
r = []
g = []
b = []
for i, s in enumerate(S):
    if s == "R":
        r.append(i)
    elif s == "G":
        g.append(i)
    else:
        b.append(i)

# print(s, r, g, b)
ans = len(r) * len(g) * len(b)
i = 0
j = 1
while i + 2 * j < n:
    while i + 2 * j < n:
        if S[i] != S[i + j] != S[i + 2 * j] != S[i]:
            ans -= 1
        i += 1
    j += 1
    i = 0

print(ans)