n = int(input())
s = input()
s_table = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i, n):
        if i != j and s[i] == s[j]:
            s_table[i][j] = 1
            s_table[j][i] = 1

# print(s_table)
ans = 0
for i in range(n):
    cnt = 0
    start = i
    j = 0
    while i < n and j < n:
        # print(i, j, start)
        if s_table[i][j] == 1 and start != j:
            # print(1)
            cnt += 1
            ans = max(cnt, ans)
        else:
            cnt = 0
            start = i + 1
        i += 1
        j += 1
print(ans)