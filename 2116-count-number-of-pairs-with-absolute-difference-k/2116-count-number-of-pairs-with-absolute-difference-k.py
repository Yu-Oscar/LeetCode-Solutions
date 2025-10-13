class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        from collections import Counter
        c = Counter(nums)

        if k == 0:
            ans = 0
            for i in c.values():
                ans += i * (i-1) // 2
            return ans

        ans = 0 
        for i in c:
            if k+i in c :
                ans += c[i] * c[i + k]
        return ans
        