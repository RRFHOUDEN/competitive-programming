s = input()
ans = 0
for i in range(1, len(s)):
    if s[i] == s[i -1]:
        ans = 1
if not ans:
    print("Good")
else:
    print("Bad")