class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while nums != sorted(nums):
            min_sum, idx = float('inf'), None
            for i in range(len(nums) - 1):
                if (curr_sum := nums[i] + nums[i + 1]) < min_sum:
                    idx, min_sum = i, curr_sum
            nums[idx] = min_sum
            nums.pop(idx + 1)
            ops += 1
        return ops