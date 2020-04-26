S = input()
S_len = len(S) - 1
p = []
for i in range(2 ** S_len):
    tmp = bin(i)[2::]
    while len(tmp) < S_len:
        tmp = "0" + tmp
    p.append(str(tmp))

sum = 0
for i in p:
    if len(p) == 1:
        sum = S
        break
    P = list(i)
    tmp = int(S[0])
    cnt = 1
    for j in P:
        if j == "0":
            tmp *= 10
            tmp += int(S[cnt])
        else:
            sum += tmp
            tmp = int(S[cnt])
        cnt += 1
    sum += tmp
print(sum)