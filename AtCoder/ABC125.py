N = list(input())

tmp = 0
for i in N:
    tmp += int(i)

ans_list = []
while tmp > 0:
    ans_list.append(str(min(9, tmp)))
    tmp -= min(9, tmp)


if len(N) == 1:
    ans_list = ["1", str(int(N[0]) - 1)]

ans_list.sort()
if ans_list[0] == "0":
    ans_list = ans_list[::-1]

ans_str = "".join(ans_list)

if ans_list == N:
    if ans_str[0] == "9":
        ans_list = ["1", "8"] + ans_list[1::]
    else:
        ans_list = [str(int(ans_list[0]) + 1), "8"] + ans_list[2::]

ans_str = "".join(ans_list)

print(ans_str)