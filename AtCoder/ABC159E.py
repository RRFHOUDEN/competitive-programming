h, w, K = map(int, input().split())
s = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        s[i][j] = int(s[i][j])
# print(s)
bit = []
if h == 1:
    ans = w // K
    if ans == w / K:
        print(ans - 1)
    else:
        print(ans)
else:
    for i in range(0, 2 ** (h - 1)):
        i_bit = bin(i)[2:]
        while len(i_bit) < len(bin(2 ** (h - 2))[2:]):
            i_bit = "0" + i_bit
        bit.append(i_bit)
    ans = 10 ** 10

    for pa in bit:
        patarn = []
        start = 0
        end = 0

        for i in range(len(pa)): #pa = 2 ** h <= 1024
            if pa[i] == "1":
                patarn.append([start, i + 1])
                start = i + 1
        patarn.append([start, h])
        # print(pa, patarn)
        area = [0 for _ in range(len(patarn))]
        cnt = len(area) - 1
        for j in range(w): #w <= 1000
            for k in range(len(area)): #len(area) <= h
                tmp = [0 for _ in range(len(patarn))]
                for i in range(patarn[k][0], patarn[k][1]): #max h
                    if s[i][j]:
                        area[k] += 1
                        tmp[k] += 1
                    if area[k] > K:
                        # print(j, 123)
                        cnt += 1
                        # print(area)
                        import copy
                        area = copy.deepcopy(tmp)
        ans = min(cnt, ans)
        # print(ans, cnt)

    print(ans)