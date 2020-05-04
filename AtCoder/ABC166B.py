n, k = map(int, input().split())
have = [1 for i in range(n)]
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        have[j - 1] = 0
print(sum(have))