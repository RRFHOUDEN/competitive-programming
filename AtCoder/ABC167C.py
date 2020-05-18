
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

n, m, X = map(int, input().split())
c = []
a = []
for i in range(n):
    ca = list(map(int, input().split()))
    c.append(ca[0])
    a.append(ca[1:])

ptarn = make_bit(n)
ans = 10 ** 10
for i in ptarn:
    money = 0
    x = [0 for _ in range(m)]
    for j in range(n):
        if i[j] == "1":
            money += c[j]
            for k in range(m):
                x[k] += a[j][k]

    if min(x) >= X:
        ans = min(ans, money)

if ans == 10 ** 10:
    ans = -1
print(ans)