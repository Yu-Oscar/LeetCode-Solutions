class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        if nums[left] < nums[right]:
            return nums[left]

        while left + 1 < right:
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        return nums[right]