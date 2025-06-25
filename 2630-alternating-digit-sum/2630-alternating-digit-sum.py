class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        ans = 0

        for i in range(len(s)):
            digit = int(s[i])
            if i % 2 == 0:
                ans += digit
            else:
                ans -= digit
        
        return ans
