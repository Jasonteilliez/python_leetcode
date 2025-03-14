class Solution:   
    def romanToInt(self, s: str) -> int:
        if (len(s) == 0): return 0

        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = 0    

        for i in range(len(s) - 1):
            if (dic[s[i]] < dic[s[i + 1]]):
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        res += dic[s[-1]]
        
        return res


s = Solution()
n = ["LVIII", "III", "MCMXCIV"]
for i in n :
    print(f"{i} is equal to {s.romanToInt(i)}")
