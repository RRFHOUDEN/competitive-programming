n, a, b = map(int, input().split())
d = list(map(int, input().split()))

d.sort()

d = [1] + d

for i in range(len(d)):
    if d[i] == n:
        del d[i + 1::]
        break
    elif d[i] > n:
        del d[i::]
        break


print(d)
ans = len(d) - 1
for i in range(1, len(d)):
    if d[i] - d[i - 1] >= a:
        ans += (d[i] - d[i - 1]) // a
    print(i, ans)

if n - d[-1] >= a:
    print(123)
    ans += (n - d[-1]) // a
print(n - ans)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] + nums[j] == taeget:
                        return [i, j]