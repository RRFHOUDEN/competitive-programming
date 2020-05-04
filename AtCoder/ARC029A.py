def make_bit(n):
    bit = []
    for i in range(2**n):
        bit.append(bin(i)[2::])
    i = 0
    while i < len(bit):
        while len(bit[i]) < n:
            bit[i] = "0" + bit[i]
        i += 1

    return bit

n = int(input())
t = [int(input()) for _ in range(n)]
bit = make_bit(n)
ans = 10 ** 10
for i in bit:
    tmp1 = 0
    tmp2 = 0
    for j in range(n):
        if i[j] == "0":
            tmp1 += t[j]
        else:
            tmp2 += t[j]
    ans = min(ans, max(tmp1, tmp2))

print(ans)