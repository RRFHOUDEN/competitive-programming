def make_bit(n):
    bit = []
    for i in range(2**n):
        bit.append(bin(i)[2::])
    i = 0
    while i < len(bit):
        while len(bit[i]) < len(bin(2**n-1)[2::]):
            bit[i] = "0" + bit[i]
        i += 1

    return bit

n = int(input())
a = []
xy_list = []
for i in range(n):
    a.append(int(input()))
    xy = [list(map(int, input().split())) for _ in range(a[i])]
    xy_list.append(xy)

# print(xy_list)

bit = make_bit(n)
ans = 0
for i in bit:
    tmp = [0 for _ in range(n)]
    NO = 0
    cnt = 0
    for j in range(n):
        if i[j] == "1":
            cnt += 1
            for x, y in xy_list[j]:
                if y and i[x-1] == "0":
                    NO = 1
                    break
                if not y and i[x-1] == "1":
                    NO = 1
                    break
        if NO:
            break

    if not NO:
        # print(i, tmp)
        ans = max(ans, cnt)
print(ans)
