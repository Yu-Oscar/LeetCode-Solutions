class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for i in range(len(nums))]

        left = 1
        for i in range(len(nums)):
            ans[i] *= left
            left *= nums[i]

        right = 1
        for i in reversed(range(len(nums))):
            ans[i] *= right
            right *= nums[i]

        return ans