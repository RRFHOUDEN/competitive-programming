w, h, a, b = map(int, input().split())

# # y = (a - w / 2)(X - a) + b
# if a == w / 2:
#     ans = w * h / 2
# elif b == h / 2:
#     ans = w * h / 2
# elif a - w / 2 >= w / h or a - w / 2 >= -1 * (w / h):
#     key = (h + a * a - w / 2 * a - b) / (a - w / 2)
#     ans = key * (w - key) * h / 2
# else:
#     key = -a * a + w / 2 * a + b
#     ans = key * ( h - key) * w / 2
ans = w * h / 2
ans2 = 0
if a == w / 2 and b == h / 2:
    ans2 = 1
print(ans, ans2)
