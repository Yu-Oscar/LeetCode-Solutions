class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mini = float('inf')

        for i in range(len(nums)+1-k):
            window = nums[i:i+k]
            mini = min(mini, window[-1]-window[0])

        return mini
