class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum = sum(nums)

        dsum = 0
        for num in nums:
            for i in str(num):
                dsum += int(i)
        
        return abs(esum - dsum)

        