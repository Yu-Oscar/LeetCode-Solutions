class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        se = set()
        for i in range(len(s)-1):
            se.add(s[i]+s[i+1])
        ans = False
        reverse = s[::-1]
        for i in range(len(reverse)-1):
            if (reverse[i]+reverse[i+1]) in se:
                ans = True
        
        return ans