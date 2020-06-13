def check_sosu(n):
    if n < 2:
        return 0
    j = 2
    while j * j <= n:
        if n % j == 0:
            return 0
        j += 1
    return 1

n = int(input())


sosu = [1 for _ in range(10**6+5)]
sosu[0] = 0
sosu[1] = 0
for i in range(2, len(sosu)):
    if sosu[i]:
        j = i+i
        while j < len(sosu):
            sosu[j] = 0
            j += i

z_list = []
z_set = set()
for i in range(2, len(sosu)):
    if sosu[i]:
        j = i
        while j <= n:
            if not j in z_set:
                z_list.append(j)
                z_set.add(j)
            j *= i



o_n = n
cnt = 0

for i in z_list:
    if n % i == 0:
        cnt += 1
        n //= i

if n >= 10**6+5:
    tmp = check_sosu(n)
    cnt += tmp

print(cnt)