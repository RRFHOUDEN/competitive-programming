n = int(input())
s = input()
ans = "No"
if n % 2 == 0:
    if s[:n // 2] == s[n // 2:]:
        ans = "Yes"

print(ans)