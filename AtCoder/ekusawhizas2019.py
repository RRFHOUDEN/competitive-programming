def this_ord(i):
    return ord(i) - ord("A")
N, Q = map(int, input().split())
s = input()
s_list = [[] for i in range(26)]
for i in range(N):
    s_list[ord(s[i]) - ord("A")].append(i)

abs_cnt = [[0, 0, 0] for i in range(len(26))]

t, d = input().split()
if d == "L":
    abs_cnt[this_ord(t)][0] -= 1
else:
    abs_cnt[this_ord(t)][0] += 1
abs_cnt[this_ord(t)][1] = min(abs_cnt[this_ord(t)][0], abs_cnt[this_ord(t)][1])
abs_cnt[this_ord(t)][2] = max(abs_cnt[this_ord(t)][0], abs_cnt[this_ord(t)][2])

for j in range(1, Q):
    t, d = input().split()
    if d == "L":
        abs_cnt[this_ord(t)][0] -= 1
    else:
        abs_cnt[this_ord(t)][0] += 1
    abs_cnt[this_ord(t)][1] = min(abs_cnt[this_ord(t)][0], abs_cnt[this_ord(t)][1])
    abs_cnt[this_ord(t)][2] = max(abs_cnt[this_ord(t)][0], abs_cnt[this_ord(t)][2])

ans = 0
for i in range(26):
    ans += len(s_list[i])

print(ans, s_list)

