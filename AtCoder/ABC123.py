x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

A = A[::-1]
B = B[::-1]
C = C[::-1]

a = 0
b = 0
c = 0

visited = [[0 for i in range(max(x, y, z))] for i in range(3)]
myA = 0
myB = 0
myC = 0

for i in range(k):
    visited[0][a] += 1
    visited[1][b] += 1
    visited[2][c] += 1

    print(a, b, c)
    print(A[a] + B[b] + C[c])
    if a == len(A) - 1:
        thisA = 10 ** 20
    else:
        thisA = A[myA] - A[a + 1]
    if b == len(B) - 1:
        thisB = 10 ** 20
    else:
        thisB = B[myB] - B[b + 1]
    if c == len(C) - 1:
        thisC = 10 ** 20
    else:
        thisC = C[myC] - C[c + 1]
    this = [thisA, thisB, thisC]

    if min(this) == thisA:
        a += 1
        for j in range((max(x, y, z))):
            if visited[1][j] < x * z:
                b = j
                myB = b
                break
        for j in range((max(x, y, z))):
            if visited[2][j] < x * y:
                c = j
                byC = c
                break

    elif min(this) == thisB:
        b += 1
        for j in range((max(x, y, z))):
            if visited[0][j] < x * z:
                a = j
                myA = a
                break
        for j in range((max(x, y, z))):
            if visited[2][j] < x * y:
                c = j
                myC = c
                break
    else:
        c += 1
        for j in range((max(x, y, z))):
            if visited[0][j] < x * z:
                a = j
                myA = a
                break
        for j in range((max(x, y, z))):
            if visited[1][j] < x * y:
                b = j
                myB = b
                break