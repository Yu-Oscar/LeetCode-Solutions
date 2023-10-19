class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for x in range(len(nums[i+1:])):
                if (nums[i] + nums[1+i+x]) == target:
                    return [i,1+i+x]

            
            
            
                