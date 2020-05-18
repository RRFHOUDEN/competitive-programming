n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

sum_i = [0 for _ in range(n)]
sum_i[0] = a[0]
for i in range(1, n):
    sum_i[i] += sum_i[i-1] + a[i]

b = [0 for _ in range(n)]
for i in range(n):
    b[i] = sum_i[i] - k*(i+1)

sorted_b = sorted(b)
print(sorted_b)
id_to_n = {}
for i in range(n):
    id_to_n[sorted_b[i]] = i

c = [0 for _ in range(n)]
for i in range(n):
    c[i] = id_to_n[b[i]]
print(b)
print(c)

cnt = 0
for i in range(n):
    for j in range(i, n):
        if i == j and b[i] >= 0:
            cnt += 1
        if i != j and b[i] >= b[j]:
            cnt += 1

print(cnt)