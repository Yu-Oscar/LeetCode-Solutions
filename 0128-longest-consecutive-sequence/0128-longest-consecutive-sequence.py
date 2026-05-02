class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        s = set(nums)

        for num in s:
            count = 1
            if (num-1) not in s:
                while (num+count) in s:
                    count += 1
            ans = max(ans, count)

        return ans
