Q = input()
f = []
f2 = [0 for i in range(Q)]
s = 0
j = 0
for i in range(Q):
    q = list(map(int, input().split()))
    if len(q) >= 1:
        f.append(q[1])
        if j == 0:
            f2[j] = q[1]
        s += q[2]
    else:
        if len(f) % 2 != 0:
            this_x = f[len(f) // 2]
        else:
            this_x = sum(f[len(f) // 2:len(f) // 2 + 2])
