n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
ba = []
for i in ab:
    ba.append(i[::-1])
ba.sort()
cnt = 1
broken = ba[0][0] - 1
for i in ba[1::]:
    if i[1] > broken:
        broken = i[0] - 1
        cnt += 1
print(cnt)