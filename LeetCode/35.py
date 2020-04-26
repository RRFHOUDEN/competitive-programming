def solve(n):
    ans = ""
    minus = 0
    if n < 0:
        minus = 1
    n = abs(n)
    while n >= 2:
        ans += str(n % 2)
        n //= 2
    ans += str(n)
    if minus:
        ans += "-"
    return ans[::-1]

# num = int(input())
num = 10 ** 120
print(solve(num))
print(int(bin(num)[2::]))