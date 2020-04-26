N, L = map(int, input().split())
rng = []
for i in range(N):
    rng.append(L + i)
minimini = 1000000000000
mini = 100000000000
for i in rng:
    if minimini > abs(i):
        mini = i
        minimini = abs(i)

print(sum(rng) - mini)