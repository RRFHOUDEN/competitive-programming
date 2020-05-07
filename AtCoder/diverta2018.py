n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
import fractions
def yakusuu(N):
    i = 1
    ans = []
    while i * i <= N:
        if N % i == 0:
            ans.append(i)
            ans.append(N // i)
        i += 1
    return ans

kouho = yakusuu(ab[0][0]) + yakusuu(ab[0][1])
kouho.sort()
i = 1
while i < len(kouho):
    if kouho[i] == kouho[i - 1]:
        del kouho[i]
        i -= 1
    i += 1

kouho = kouho[::-1]
ans = 0
key = 1
for i in kouho:
    key = 1
    for j, k in ab:
        #print(i, j, k)
        if j % i == 0 or k % i == 0:
            key = min(1, key)
        else:
            key = 0
            break

    if key == 1:
        ans = i
        break

print(ans)