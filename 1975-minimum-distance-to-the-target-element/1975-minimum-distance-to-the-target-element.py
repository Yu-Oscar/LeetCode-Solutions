class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        for d in range(n):
            left = start - d
            right = start + d
            if 0 <= left and nums[left] == target:
                return d
            if right < n and nums[right] == target:
                return d