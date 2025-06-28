class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        sums = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left == (sums - nums[i] - left):
                return i
            
            left += nums[i]

        return -1
            
