class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)

        for i in range(len(nums)+1):
            if i in s:
                s.remove(i)
            else:
                return i
        
        