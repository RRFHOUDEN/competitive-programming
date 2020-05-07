import  fractions
n = int(input())
s = input()
inv_cnt = []
cnt1 = 0
cnt2 = 0
for i in s:
    if i == "B":
        inv_cnt.append(1)
        cnt1 += 1
    else:
        inv_cnt.append(2)
        cnt2 += 1

if cnt1 <= 1 or cnt2 <= 1:
    ans = 0
else:
    ans = fractions.factorial(cnt1 - 1)
    ans %= 10 ** 9 + 7
# print(ans)
    ans += fractions.factorial(cnt2 - 1)
    ans %= 10 ** 9 + 7
# print(ans)
    ans *= fractions.factorial(n)
    ans %= 10 ** 9 + 7

# ans = 1
# key = 1
# # print(inv_cnt)
# yokuwakaranairisuto = [key]
# for i in range(1, 2 * n):
#     if inv_cnt[i] != inv_cnt[i - 1]:
#         # print(i, inv_cnt[i])
#         key += 1
#     yokuwakaranairisuto.append(key)
#
# yokuwakaranairisuto[-1] = 1
# key = 1
# for i in range(2 * n - 2, 0, -1):
#     if inv_cnt[i] != inv_cnt[i + 1]:
#         # print(i, inv_cnt[i])
#         key += 1
#     yokuwakaranairisuto[i] = min(yokuwakaranairisuto[i], key)
# # print(yokuwakaranairisuto)
#
# ans = 1
# for i in range(1, 2 * n):
#     if yokuwakaranairisuto[i] != yokuwakaranairisuto[i - 1]:
#         ans *= yokuwakaranairisuto[i]
#         ans %= 10 ** 9 + 7
# if ans == 1:
#     ans = 0
# ans *= fractions.factorial(n)
ans %= 10 ** 9 + 7
print(ans)