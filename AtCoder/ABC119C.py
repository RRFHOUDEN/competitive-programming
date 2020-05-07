N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]

def DFS(cnt, a, b, c):
    if cnt == N:
        # print(cnt, a, b, c)
        if a == 0 or b == 0 or c == 0:
            return 10 ** 10
        return abs(A-a) + abs(B-b) + abs(C-c) - 30

    r1 = DFS(cnt+1, a, b, c)
    r2 = DFS(cnt+1, a+l[cnt], b, c) + 10
    r3 = DFS(cnt+1, a, b+l[cnt], c) + 10
    r4 = DFS(cnt+1, a, b, c+l[cnt]) + 10
    return min(r1, r2, r3, r4)

print(DFS(0, 0, 0, 0))