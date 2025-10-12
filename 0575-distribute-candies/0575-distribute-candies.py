class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = len(set(candyType))
        n = len(candyType)
        return min(s, n//2)