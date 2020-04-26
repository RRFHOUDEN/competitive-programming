n = int(input())
ans = n / 1.08
ans = int(ans)
if int(ans * 1.08) == n:
    print(ans)
elif int((ans + 1) * 1.08) == n:
    print(ans + 1)
else:
    print(":(")