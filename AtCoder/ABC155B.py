n = int(input())
a = list(map(int, input().split()))
ans = "APPROVED"
for i in a:
    if i % 2 == 0:
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            ans = "DENIED"
            break
    if ans == "DENIED":
        break

print(ans)