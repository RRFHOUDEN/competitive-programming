n = input()
k = 0
pay = 0
n_list = []
for i in n[::-1]:
    n_list.append(int(i))
n_list.append(0)
ans = 0
for i in range(len(n_list) - 1):
    num = n_list[i]
    if num < 5:
        ans += num
    elif (num <= 5 and n_list[i + 1] < 5):
        ans += num
    else:
        n_list[i + 1] += 1
        ans += 10 - num

ans += n_list[-1]
print(ans)