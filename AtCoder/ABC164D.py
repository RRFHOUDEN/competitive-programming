S = input()
for i in range(len(S)):
    for j in range(i, len(S)):
        if int(S[i:j+1]) % 2019 == 0 and int(S[i:i+1]) != 0:
            print(i, j)
            print(S[i:j + 1])
#
for i in range(100001):
    check = 0
    cnt = 0
    for j in str(2019 * i):
        # print(j)
        if j == "0":
            check = 1
            break
        cnt += int(j)
    if check:
        continue
    print(2019 * i, cnt)
