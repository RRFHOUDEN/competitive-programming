while 1:
    def solved(nums, k):
        nums.sort()
        cnt = 1
        nums_cnt = []
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums_cnt.append([cnt, nums[i - 1]])
                cnt = 1
            else:
                cnt += 1
        nums_cnt.append([cnt, nums[-1]])
        nums_cnt.sort()
        nums_cnt = nums_cnt[::-1]
        # print(nums_cnt)
        ans = []
        for i in range(k):
            ans.append(nums_cnt[i][1])
        return ans
    print(solved([4,1,-1,2,-1,2,3], 2))
    break