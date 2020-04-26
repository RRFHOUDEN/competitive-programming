n = int(input())
a = list(map(int, input().split()))
cnt0 = 0
cnt1 = 0
for num in a:
    num = bin(num)[2::]
    # print(num)
    tmp = 0
    for i in num:
        tmp = tmp ^ int(i)
    # print(tmp)
    if tmp:
        cnt1 += 1
    else:
        cnt0 += 1
print(cnt0, cnt1)
if abs(cnt1 - cnt0) == 1:
    print("Yes")
else:
    print("No")