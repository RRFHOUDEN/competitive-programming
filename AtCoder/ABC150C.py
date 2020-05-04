def make(nums, now):
    # print(nums, now)
    if len(nums) == 0:
        dic.append(now)

    for i in range(len(nums)):
        tmp = nums[:i]
        if i+1 < len(nums):
            tmp += nums[i+1:]
        make(tmp, now+[nums[i]])

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
dic = []
original_nums = [i for i in range(1, n+1)]
make(original_nums, [])
for i in range(len(dic)):
    if dic[i] == p:
        num_p = i
    if dic[i] == q:
        num_q = i
# print(num_p, num_q)
print(abs(num_q - num_p))
