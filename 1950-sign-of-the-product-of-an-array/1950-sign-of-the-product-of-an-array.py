class Solution:
    def arraySign(self, nums: List[int]) -> int:
        import math 
        ans = math.prod(nums)
        if ans == 0:
            return 0
        elif ans > 0:
            return 1
        else:
            return -1
        