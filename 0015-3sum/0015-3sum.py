class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue 
            
            curr = nums[i]

            left = i+1
            right = len(nums)-1
            while left < right:
                val = curr + nums[left] + nums[right]

                if val == 0:
                    ans.append([curr, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif val < 0:
                    left += 1
                else:
                    right -= 1
            
            i += 1
            
        return ans