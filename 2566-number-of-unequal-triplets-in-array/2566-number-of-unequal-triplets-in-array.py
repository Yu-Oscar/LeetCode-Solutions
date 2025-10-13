class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        from collections import Counter
        from itertools import combinations
        
        n = len(nums)
        s = set(nums)
        c = Counter(nums)
        ans = 0

        for x, y, z in combinations(s, 3):
            ans += c[x] * c[y] * c[z]
        
        return ans
        