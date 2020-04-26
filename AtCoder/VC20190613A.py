s = input()
n = len(s)
cnt = [[] for i in range(26)]

j = 0
for i in s:
    cnt[ord(i) - ord("a")].append(j)
    j += 1

ans = 0
def BFS(q, now, L, visited):
    global ans
    print(q, now)
    i = q[now]
    ans += 1
    visited[i] = 1
    if sum(visited) == L:
        return cnt
    if i > 0 and not visited[i - 1]:
        q.append(i - 1)
    if i < L - 1 and not visited[i + 1]:
        q.append(i + 1)
    now += 1
    if now >= len(q):
        return ans
    BFS(q, now, L, visited)
    return ans

for i in range(26):
    a = cnt[i]
    visited = [0 for i in range(n)]
    if len(a) != 0:
        print(chr(i + ord("a")))
        print(BFS(a, 0, n, visited))
