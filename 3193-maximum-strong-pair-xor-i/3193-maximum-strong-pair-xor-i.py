class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        l = 0
        maxor = 0

        while l < len(nums):
            for r in nums[l:]:
                pair = abs(nums[l] - r)
                if pair <= min(nums[l], r):
                    maxor = max(maxor, nums[l] ^ r)
            l += 1
        
        return maxor

        