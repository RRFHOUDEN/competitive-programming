list = input().split(" ")
h = int(list[0])
w = int(list[1])
n = int(list[2])

list = input().split(" ")
y = int(list[0])
x = int(list[1])

# l,r,u,d
ato = [x, w - x + 1, y, h - y + 1]
countt = [0, 0, 0, 0]
counta = [0, 0, 0, 0]
counta2 = [0, 0, 0, 0]  # dokudan
kano = [0, 0, 0, 0]
# print(ato)

taka = input()
aoki = input()

switch = 0

for i in range(n):
    if i > 0:
        if aoki[i - 1] == 'L':
            if counta[0] - countt[1] < x - 1:
                counta[0] += 1
        elif aoki[i - 1] == 'R':
            if counta[1] - countt[0] < w - x:
                counta[1] += 1
        elif aoki[i - 1] == 'U':
            if counta[2] - countt[3] < y - 1:
                counta[2] += 1
        elif aoki[i - 1] == 'D':
            if counta[3] - countt[2] < h - y:
                counta[3] += 1

    if taka[i] == 'L':
        countt[0] += 1
    elif taka[i] == 'R':
        countt[1] += 1
    elif taka[i] == 'U':
        countt[2] += 1
    elif taka[i] == 'D':
        countt[3] += 1

    countn = [countt[0] - counta[1], countt[1] - counta[0], countt[2] - counta[3], countt[3] - counta[2]]

    # print(countn)
    for j in range(4):
        if countn[j] >= ato[j]:
            switch = 1

if switch == 1:
    print('NO')
else:
    print('YES')
