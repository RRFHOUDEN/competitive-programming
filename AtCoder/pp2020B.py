h, w = map(int, input().split())
ans = h * w // 2
if h == 1 or w == 1:
    print(1)
elif h * w % 2 == 0:
    print(ans)
else:
    print(ans + 1)