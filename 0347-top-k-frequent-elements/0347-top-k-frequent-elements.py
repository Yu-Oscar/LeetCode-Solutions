import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        heap = [(-value, key) for key, value in counts.items()]
        heapq.heapify(heap)

        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(heap)[1])

        return ans