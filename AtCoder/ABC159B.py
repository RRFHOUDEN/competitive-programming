def check(s):
    # print(s)
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def solve():
    s = input()
    if not check(s):
        return "No"
    # print(s[:(len(s) - 1) // 2 + 1], 111, (len(s) - 1) // 2 + 1, (len(s) + 3)// 2)
    if not (check(s[:(len(s) - 1) // 2])):
        return "No"
    if not check(s[(len(s) + 3)// 2 - 1:]):
        return "No"
    return "Yes"

print(solve())