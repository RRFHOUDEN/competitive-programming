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