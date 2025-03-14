class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i, n in enumerate(nums):
            if target - n in h:
                return [h[target - n], i]
            h[nums[i]] = i
        return []


s = Solution()
n = [
    {"nums":[2,7,11,15], "target":9},
    {"nums":[3,2,4], "target":6},
    {"nums":[3,3], "target":6}
]
for i in n :
    print(f"the two sum of {i["nums"]} with target {i["target"]} is {s.twoSum(i["nums"],i["target"])}")