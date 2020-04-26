while 1:
    def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        for i in range(len(strs)):
            strs[i] = [sorted(list(strs[i])), strs[i]]

        strs.sort()
        ans = [[strs[0][1]]]
        now = 0
        print(strs)
        for i in range(1, len(strs)):
            if strs[i][0] == strs[i - 1][0]:
               ans[now].append(strs[i][1])
            else:
                ans.append([strs[i][1]])
                now += 1
        return ans

    print(groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))
    break