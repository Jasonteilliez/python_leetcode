class Solution:


    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False 
        return str(x) == str(x)[::-1]
    

    def isPalindromeWithoutString(self, x: int) -> bool:
        if x < 0 : return False
        
        n = x
        rev = 0
        while(n > 0):
            a = n % 10
            rev = rev * 10 + a
            n = n // 10

        if rev == x: return True
        return False


s = Solution()
n = [121, -121, 10]
for i in n :
    print(f"Is {i} a palindrome : {s.isPalindrome(i)}")



