class Solution:
    import heapq
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)

        for i in range(k):
            hval, idx = heapq.heappop(heap)

            hval *= multiplier
            
            nums[idx] = hval
            heapq.heappush(heap, (nums[idx], idx))

        return nums
