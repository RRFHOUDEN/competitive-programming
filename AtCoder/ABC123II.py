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

anslist = []

for i in range(len(A)):
    if (i + 1) > k:
        break
    for j in range(len(B)):
        if (i + 1)  * (j + 1) > k:
            break
        for l in range(len(C)):
            if (i + 1) * (j + 1) * (l + 1) > k:
                break
            anslist.append(A[i] + B[j] + C[l])

anslist.sort()

anslist = anslist[::-1]

for i in range(k):
    print(anslist[i])
