import itertools
h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
s_list = []
y = 0
x = 0
for i in s:
    for j in i:
        if j == "o":
            s_list.append([x, y])
        x += 1
    y += 1
    x = 0

p = itertools.permutations(s_list, len(s_list))
if len(s_list) > 8:
    print(191919210813089342809)
else:
    key = True
    for i in p:
        key = True
        for j in range(1, len(i)):
            if j > 1:
                if i[j][0] == i[j - 2][0] or i[j][1] == i[j - 2][1]:
                    key = False
                    break
            if not key:
                break
            if i[j][0] != i[j - 1][0] and i[j][1] != i[j - 1][1]:
                key = False
                break
        if key:
            print("Possible")
            break

    if not key:
        print("Impossible")
