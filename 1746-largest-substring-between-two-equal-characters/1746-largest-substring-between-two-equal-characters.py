class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ans = -1 

        for i, x in enumerate(s):
            if x not in first:
                first[x] = i
            else:
                ans = max(ans, i-first[x]-1)
        
        return ans