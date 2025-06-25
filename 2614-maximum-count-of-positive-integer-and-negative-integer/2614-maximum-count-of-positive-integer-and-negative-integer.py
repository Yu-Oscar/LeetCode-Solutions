class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        #find largest -ve
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid
        
        neg = left
        
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid + 1 
            else:
                right = mid
        
        return max(neg, n - left)

            

