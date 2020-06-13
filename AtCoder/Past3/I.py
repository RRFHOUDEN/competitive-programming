def cal_a(i, j):
    return n*i + j

n = int(input())
q = int(input())
r = [i for i in range(n)]
c = [i for i in range(n)]
tenchi = 1

for i in range(q):
    q = list(map(int, input().split()))
    if (q[0] == 1 and tenchi == 1) or (q[0] == 2 and tenchi == -1):
        r[q[1]-1], r[q[2]-1] = r[q[2]-1], r[q[1]-1]
    elif (q[0] == 2 and tenchi == 1) or (q[0] == 1 and tenchi == -1):
        c[q[1]-1], c[q[2]-1] = c[q[2]-1], c[q[1]-1]
    elif q[0] == 3:
        tenchi *= -1
    else:
        # print(q[1], q[2])
        if tenchi == 1:
            print(cal_a(r[q[1]-1], c[q[2]-1]))
        else:
            print(cal_a(r[q[2]-1], c[q[1]-1]))
    # print(r)
    # print(c)
    # print(i, tenchi, q)
    # print()

# print(r)
# print(c)