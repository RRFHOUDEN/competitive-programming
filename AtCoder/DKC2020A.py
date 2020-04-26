N = int(input())
s_list = []
t_list = []
for i in range(N):
    s, t = input().split()
    s_list.append(s)
    t_list.append(int(t))

x = input()
ans = 0
for i in range(N):
    ans += t_list[i]
    if x == s_list[i]:
        break
print(sum(t_list) -  ans)