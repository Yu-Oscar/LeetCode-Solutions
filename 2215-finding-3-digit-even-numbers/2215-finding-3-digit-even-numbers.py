class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(digits)
        ans = []
        for num in range (100,1000, 2):
            parts = [num // 100, (num // 10) % 10, num % 10]
            count = Counter(parts)
            if all(c[d] >= count[d] for d in count):
                ans.append(num)

        return ans
        