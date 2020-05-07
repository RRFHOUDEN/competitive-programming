n = int(input())
s_lsit = {}
cnt = 0
for i in range(n):
    s = list(input())
    s.sort()
    s = "".join(s)
    if s in s_lsit:
        cnt += s_lsit[s]
        s_lsit[s] += 1
    else:
        s_lsit[s] = 1
print(cnt)