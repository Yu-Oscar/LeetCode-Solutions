class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        c = Counter(arr)
        for char in arr:
            if c[char] == 1:
                k -= 1
                if k == 0:
                    return char
        return ""
