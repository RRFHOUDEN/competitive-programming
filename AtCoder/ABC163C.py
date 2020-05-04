n = int(input())
a = list(map(int, input().split()))
cnt = [0 for _ in range(n)]
for i in a:
    cnt[i-1] += 1
for i in cnt:
    print(i)