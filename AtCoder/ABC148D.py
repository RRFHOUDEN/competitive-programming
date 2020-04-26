import sys
sys.setrecursionlimit(100000)
def sarach(now, before, tree, target, cnt):
    print(now, target)
    if now == target:
        return cnt
    for i in range(len(tree[now])):
        # print(now, i, tree[now][i])
        if tree[now][i] != before:

            # print(tree[now][i], now, i)
            ans = sarach(tree[now][i], now, tree, target, cnt+1)
            if ans != None:
                return ans

n, u, v = map(int, input().split())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
print(tree)
print(sarach(v - 1, -1, tree, u - 1, 0))