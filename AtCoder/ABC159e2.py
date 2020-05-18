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

h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]
one_zero = make_bit(h-1)

for i in one_zero:
    print(i)
    be = []
    begin = 0
    end = 0
    for j in range(h-1):
        end = j+1
        if i[j] == "1":
            be.append([begin, end])
            begin = end
    end += 1
    be.append([begin, end])
    print(be)