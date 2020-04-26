def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

n = int(input())
out = make_divisors(n)
ans = []
for i in out:
    if i == 1:
        continue
    m = n
    while m % i == 0:
        m //= i
    if m == 1 or m % i == 1:
        ans.append(i)
ans += make_divisors(n - 1)
# print(set(out))
print(len(set(ans)) - 1)