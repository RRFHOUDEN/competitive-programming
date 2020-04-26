n = int(input())
a = list(map(int, input().split()))

color = [0 for i in range(n)]
patarn = [0 for _ in range(n + 1)]
color[0] = 3

for i in range(1, n):
    color[i] += patarn[a[i] - 1]
    patarn[a[i]] = color[i]



print(color)
ans = color[-1] % 1000000007


print(ans)