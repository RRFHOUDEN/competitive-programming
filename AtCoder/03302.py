N, Q = map(int, input().split())
s = input()
s_list = [[] for i in range(26)]
for i in range(N):
    s_list[ord(s[i]) - ord("A")].append(i)

for j in range(Q):
    t, d = input().split()
    if d == "L":
        for i in range(len(s_list[ord(t) - ord("A")])):

            s_list[ord(t) - ord("A")][i] -= 1
    else:
        for i in range(len(s_list[ord(t) - ord("A")])):
            s_list[ord(t) - ord("A")][i] += 1

    i = 0
    while len(s_list[ord(t) - ord("A")]) > i:
        if s_list[ord(t) - ord("A")][i] < 0 or  s_list[ord(t) - ord("A")][i] >= N:
            del s_list[ord(t) - ord("A")][i]
            i -= 1
        i += 1
    print(j, s_list)
ans = 0
for i in range(26):
    ans += len(s_list[i])

print(ans, s_list)

