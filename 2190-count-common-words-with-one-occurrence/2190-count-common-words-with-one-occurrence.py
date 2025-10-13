class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        c1 = set([n for n in words1 if Counter(words1)[n] == 1])
        c2 = set([n for n in words2 if Counter(words2)[n] == 1])
        return len(c1 & c2)