k = int(input())
a, b = map(int, input().split())
tmp = 0
for i in range(a, b+1):
    if i % k == 0:
        tmp = 1
if tmp:
    print("OK")
else:
    print("NG")