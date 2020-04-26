ABCD = list(input())
p_m = []
for i in range(2 ** 3):
    tmp = bin(i)[2::]
    while len(tmp) < 3:
        tmp = "0" + tmp
    p_m.append(tmp)

for i in p_m:
    sum = int(ABCD[0])
    cnt = 1
    plusminus = []
    for j in i:
        # print(j, sum, cnt)
        if j == "1":
            sum += int(ABCD[cnt])
            plusminus.append("+")
        else:
            sum -= int(ABCD[cnt])
            plusminus.append("-")
        cnt += 1
    if sum == 7:
        for i in range(3):
            print(ABCD[i], end = "")
            print(plusminus[i], end = "")
        print(ABCD[3] + "=7")
        break