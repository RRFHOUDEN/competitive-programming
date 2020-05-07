n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(n)]
ans = []
for i in range(n, 0, -1):
    if a[i-1] == 0:
        tmp = 0
        j = i * 2
        while j < n:
            # print(j)
            tmp += b[j-1]
            j += i
        if tmp % 2 == 0:
            b[i-1] = 0
        else:
            b[i-1] = 1
    else:
        tmp = 0
        j = i * 2
        while j < n:
            # print(j-1)
            tmp += b[j-1]
            j += i
        if tmp % 2 == 1:
            b[i-1] = 0
        else:
            b[i-1] = 1

for i in range(n):
    if b[i] % 2 != 0:
        # print(b[i]%2)
        ans.append(a[i+1])
# print(b)
print(len(ans))
for i in ans:
    print(i)