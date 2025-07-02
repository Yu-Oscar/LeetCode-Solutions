class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        longest = 0 
        
        for i in range(n):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                length = 1

                for j in range(i+1, n):
                    if nums[j] % 2 != nums[j - 1] % 2 and nums[j] <= threshold:
                        length += 1
                    else:
                        break

                longest = max(longest, length)
        
        return longest