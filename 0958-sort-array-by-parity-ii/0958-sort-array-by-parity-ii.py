class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even, odd = 0, 1
        ans = [0] * n

        for num in nums:
            if num % 2 == 0:
                ans[even] = num
                even += 2
            else:
                ans[odd] = num
                odd += 2
        
        return ans

        