class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = [0 for _ in range(26)]
        for i in s:
            dic[ord(i) - ord("a")] += 1

        for i in s:
            if dic[ord(i) - ord("a")] == 1:
                return i