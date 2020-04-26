t = int(input())
ans = []
for i in range(t):
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for j in a:
        if b >= j:
            cnt += 1
            b -= j
        else:
            break
    ans.append(cnt)

for i, j in enumerate(ans):
    # print(f'Case #{i}: {j}')
    print("Case #" + str(i + 1) + ": " + str(j))