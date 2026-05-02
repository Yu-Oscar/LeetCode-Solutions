import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for i in range(len(nums))]
        for key, value in counts.items():
            buckets[value-1].append(key)

        ans = []
        for bucket in reversed(buckets):
            for item in bucket:
                ans.append(item)
                if len(ans) == k:
                    return ans
