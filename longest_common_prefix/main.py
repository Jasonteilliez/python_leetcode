class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        p=""
        for i in range(len(prefix)):
            c = prefix[i]
            for s in strs:
                if i == len(s):
                    return p
                if s[i] != c:
                    return p
            p += c
        return p
                
                
s = Solution()
n = [
    ["flower","flow","flight"],
    ["dog","racecar","car"],
]

for i in n :
    print(f"The longest common prefix of {i} is : '{s.longestCommonPrefix(i)}'")

