while 1:
    def solve(nums1, nums2):
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        nums1.sort()
        nums2.sort()
        newnums1 = [nums1[0]]
        newnums2 = [nums2[0]]

        for i in range(1, len(nums1)):
            if nums1[i] != nums1[i - 1]:
                newnums1.append(nums1[i])

        for i in range(1, len(nums2)):
            if nums2[i] != nums2[i - 1]:
                newnums2.append(nums2[i])

        newnums1.sort()
        newnums2.sort()
        ans = []
        for i in newnums1:
            for j in newnums2:
                if i == j:
                    ans.append(i)
        return ans


    a=[4, 9, 5]
    b=[9, 4, 9, 8, 4]
    print(solve(a, b))
    break