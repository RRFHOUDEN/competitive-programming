n, k = map(int, input().split())
s, p, r = map(int, input().split())
t = input()
output = []
ans = 0
for i in range(n):
    if i < k:
        if t[i] == "r":
            ans += r
            output.append("r")
        if t[i] == "p":
            ans += p
            output.append("p")
        if t[i] == "s":
            ans += s
            output.append("s")
    else:
        if t[i] == output[i-k]:
            output.append(1)
        else:
            if t[i] == "r":
                ans += r
                output.append("r")
            if t[i] == "p":
                ans += p
                output.append("p")
            if t[i] == "s":
                ans += s
                output.append("s")

print(ans)