n = int(input())
a = list(map(int, input().split()))
bin_a = []
for i in a:
    bin_a.append(bin(i)[2::])
maxlen = 0
for i, j in enumerate(bin_a):
    maxlen = max(maxlen, len(j))

for i, j in enumerate(bin_a):
    while len(bin_a[i]) < maxlen:
        bin_a[i] = "0" + bin_a[i]

ans = 0
for i in range(maxlen):
    zerocnt = 0
    onecnt = 0
    for j in range(len(bin_a)):
        if bin_a[j][i] == "0":
            zerocnt += 1
        else:
            onecnt += 1
    ans += zerocnt * onecnt * 2 ** i

ans %= 10 ** 9 + 7
print(bin_a)
print(ans)