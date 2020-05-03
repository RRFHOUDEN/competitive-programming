n, m = map(int, input().split())
out = []
cnt = 0
left = 0
visited = [0 for _ in range(n)]
visited[0] = 1
# print(visited)
for i in range(m+1, 0, -1):
    out.append([left, left+i])
    # print(left, left+i)
    visited[left] = 1
    visited[left+i] = 1
    if i == 0:
        break
    # print(i, visited)
    while visited[left] or visited[left+i+1]:
        # print(left)
        left += 1
# print(out)
for i, j in out:
    print(i+1, j+1)