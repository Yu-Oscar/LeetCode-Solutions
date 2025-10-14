class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        ans = 0
        for key in c.keys():
            if key+1 in c:
                ans = max(ans, c[key]+c[key+1])
        
        return ans