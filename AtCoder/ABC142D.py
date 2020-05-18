a, b = map(int, input().split())

prime_a = []
prime_b = []

o_a = a
o_b = b

i = 2
while i * i <= a:
    if a % i == 0:
        prime_a.append(i)
        prime_a.append(a//i)
    i += 1

i = 2
while i * i <= b:
    if b % i == 0:
        prime_b.append(i)
        prime_b.append(b//i)
    i += 1

prime_a.sort()
prime_b.sort()

i_a = 0
i_b = 0

same = []
while i_a < len(prime_a) and i_b < len(prime_b):
    if prime_a[i_a] == prime_b[i_b]:
        same.append(prime_a[i_a])
        i_a += 1
        i_b += 1
    elif prime_a[i_a] < prime_b[i_b]:
        i_a += 1
    else:
        i_b += 1

print(prime_a)
print(prime_b)
print(same)
print(3**len(same) * 2**(len(prime_a)-len(same)) * 2**(len(prime_b)-len(same)))
