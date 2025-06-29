class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        sorted_keys = sorted(freq)

        smaller_count = {}
        prefix_sum = 0
        for key in sorted_keys:
            smaller_count[key] = prefix_sum
            prefix_sum += freq[key]

        return [smaller_count[num] for num in nums]
        