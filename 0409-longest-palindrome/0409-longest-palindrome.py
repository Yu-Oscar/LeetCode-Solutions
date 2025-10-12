class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        ans = 0
        odd = False
        for c in Counter(list(s)).values():
            ans += (c // 2) * 2
            if c % 2 == 1:
                odd = True
        return ans + (1 if odd else 0)