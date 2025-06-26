class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        
        for _ in range(k):
            val = heapq.heappop(nums)
            heapq.heappush(nums, -val)

        return sum(nums)
        