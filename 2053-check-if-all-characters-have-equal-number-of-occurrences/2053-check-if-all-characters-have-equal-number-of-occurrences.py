class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        c = Counter(s)
        count = next(iter(c.values()))
        if all(c[i] == count for i in c):
            return True
        else:
            return False
            
        