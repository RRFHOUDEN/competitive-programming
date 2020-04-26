#
# def modinv(a, m):
#     b = m
#     u = 1
#     v = 0
#     while b:
#         t = a // b
#         a -= t * b
#         a, b = b, a
#         u -= t * v
#         u, v = v, u
#     u %= m
#     if u < 0:
#         u += m
#     return u
#
# def modpow(a, n, mod, key):
#     res = a
#     tmp = 1
#     while n > 1:
#         # print(n)
#         if n % 2 == 0:
#             if res % mod > key:
#                 res = int(res * res % mod)
#             else:
#                 res = res * res
#                 n //= 2
#         else:
#             n -= 1
#             tmp *= 2
#         #
#         # if n and 1:
#         #     if res % mod > key:
#         #         res = int(res * a % (mod))
#         #     else:
#         #         res = res * a
#         # if a * a % mod > key:
#         #     a = a * a % (mod)
#         # else:
#         #     a *= a
#         # n //= 2
#     return res * tmp

def modpow(a, n, mod, key):
    res = a
    tmp = 1
    while n > 1:
        if n % 2 == 0:
            res = int(res * res % mod)
            n //= 2
        else:
            n -= 1
            tmp *= 2
    return res * tmp % mod

# MOD = 1000000007
#
# a = 12345678900000
# b = 100000

def comb(n, k, mod):
    ans = 1
    for i in range(k - 1, -1, -1):
        ans *= (n - i) / (k - i)
        # ans %= mod
        # print(ans)
        # print(i, ans)
    print(ans)
    return ans
#
# a %= MOD
# print(a * modinv(b, MOD) % MOD)

n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
key = - comb(n, a, mod) - comb(n, b, mod) - 1
key *= -1
key %= mod
ans = modpow(2, n, mod, key) - key
print(modpow(2, n, mod, key), key)
if ans < 0:
    ans += mod
print(ans % mod)
