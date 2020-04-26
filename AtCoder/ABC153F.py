def factorization(n):
    global GCM
    arr = []
    temp = n
    now = 0
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            if len(GCM) != 0:
                GCM.append([i, cnt])

            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


GCM = []
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    GCM = GCM + factorization(a[i])
GCM.sort()
print(GCM)
gcd = []
before = 1
for i in range(len(GCM)):
    if GCM[i] == before:
        gc