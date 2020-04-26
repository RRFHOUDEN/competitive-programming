n, s = map(int, input().split())
a = list(map(int, input().split()))
pair = []
import copy
wa = copy.deepcopy(a)
for i in range(1, n):
    wa[i] += wa[i - 1]
wa = [0] + wa
n += 1
for i in range(n):
    for j in range(i, n):
        if wa[j] - wa[i - 1] == s:
            pair.append([i, j])
print(wa)
ans = 0
for i, j in pair:
    print(i, j)
    ans += i * (n - j)
    print(ans)
print(ans)