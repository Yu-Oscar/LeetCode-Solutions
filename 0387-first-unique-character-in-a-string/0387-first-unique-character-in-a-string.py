class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        for i, x in enumerate(list(s)):
            if c[x] == 1:
                return i
        return -1