import math
n = int(input())
x = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

for L in range(n):
    for R in range(n):
        if R <= L:
            continue
        