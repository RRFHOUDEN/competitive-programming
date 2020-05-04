def make(n, A, M):
    if n == 0:
        A_list.append(A)
        return
    for i in range(A[-1], M+1):
        make(n-1, A+[i], M)

n, M, q = map(int, input().split())
A_list = []
for i in range(1, M+1):
    make(n, [i], M)
# print(A_list)

abcd = [list(map(int, input().split())) for _ in range(q)]
ans = 0
for i in A_list:
    tmp = 0
    for a,b,c,d in abcd:
        if i[b] - i[a] == c:
            tmp += d
    ans = max(ans, tmp)

print(ans)