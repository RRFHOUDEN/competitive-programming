n, q = map(int, input().split())
contena = [{'mae':-1, 'ushiro':-1} for _ in range(n)]
desk = [i for i in range(n)]

for i in range(q):
    f, t, x = map(int, input().split())
    f -= 1
    t -= 1
    x -= 1

    ushiro = desk[f]
    desk[f] = contena[x]['mae']
    if desk[f] != -1:
        contena[desk[f]]['ushiro'] = -1

    if desk[t] != -1:
        contena[desk[t]]['ushiro'] = x
    contena[x]['mae'] = desk[t]
    desk[t] = ushiro

#     print(desk)
#     print(contena)
#     print()
#
# print(desk)
# print(contena)
res = [0 for _ in range(n)]
for i in range(n):
    j = desk[i]
    if j == -1:
        continue
    res[j] = i+1
    # print(i, j, res)
    while contena[j]['mae'] != -1:
        j = contena[j]['mae']
        res[j] = i+1

for i in res:
    print(i)
