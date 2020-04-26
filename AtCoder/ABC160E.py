x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort()
q.sort()
r.sort()
p = p[::-1]
q = q[::-1]
r = r[::-1]

ir = 0
ig = 0

red = 0
for i in range(x):
    red += p[i]
    ir = i
green = 0
for i in range(y):
    green += q[i]
    ig = i

ino = 0
while (0 <= ir or 0 <= ig) and ino < c:
    iir = ir
    iig = ig
    iino = ino

    if ig < 0:
        if p[ir] < r[ino]:
            red -= p[ir]
            red += r[ino]
            ino += 1
            ir -= 1
    elif ir < 0:
        if q[ig] < r[ino]:
            green -= q[ig]
            green += r[ino]
            ino += 1
            ig -= 1
    elif p[ir] < q[ig]:
        if p[ir] < r[ino]:
            red -= p[ir]
            red += r[ino]
            ino += 1
            ir -= 1
    else:
        if q[ig] < r[ino]:
            green -= q[ig]
            green += r[ino]
            ino += 1
            ig -= 1

    if iir == ir and iig == ig and iino == ino:
        break

print(green + red)
