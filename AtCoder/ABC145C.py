import math
import itertools

ans = 0

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
root = [i for i in range(n)]
roots = list(itertools.permutations(root))
for i in roots:
    for j in range(1, n):
        ans += math.sqrt(((xy[i[j - 1]][0] - xy[i[j]][0]) ** 2 +  (xy[i[j - 1]][1] - xy[i[j]][1]) ** 2))


print(ans / len(roots))