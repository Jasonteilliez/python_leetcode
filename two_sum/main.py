class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i, n in enumerate(nums):
            if target - n in h:
                return [h[target - n], i]
            h[nums[i]] = i
        return []


s = Solution()
print(s.twoSum([0,0,3,4], 4))