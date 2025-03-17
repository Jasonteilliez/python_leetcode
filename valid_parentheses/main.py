class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        braces = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in braces.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or braces[stack.pop()] != c:
                    return False
        return len(stack) == 0 


s = Solution()
n = ["()","()[]{}","(]","([])"]
for i in n :
    print(f"Is {i} valid parentheses : {s.isValid(i)}")
