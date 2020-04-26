def lengthOfLongestSubstring(s: str) -> int:
    count = [0 for i in range(26)]
    cnt = 0
    ans = 0
    check = "\" \""
    if s == check:
        return 0
    for i in range(len(s)):
        if not count[ord(s[i]) - ord("a")]:
            cnt += 1
            count[ord(s[i]) - ord("a")] = 1
        else:
            ans = max(ans, cnt)
            count = [0 for i in range(26)]
            count[ord(s[i]) - ord("a")] = 1
            cnt = 1

    ans = max(ans, cnt)
    return ans


s = input()
print(lengthOfLongestSubstring(s))

for i in s:
            if i == " ":
                zero_cnt += 1
            else:
                new_s += i
        s = new_s
        if zero_cnt == len(s):
            return 0