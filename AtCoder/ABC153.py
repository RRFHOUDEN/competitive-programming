h, a = map(int, input().split())

ans = h / a
if int(ans) == ans:
    print(int(ans))
else:
    print(int(ans) + 1)