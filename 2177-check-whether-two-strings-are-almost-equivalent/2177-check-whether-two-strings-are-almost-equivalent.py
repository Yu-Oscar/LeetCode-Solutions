class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        c1, c2 = Counter(word1), Counter(word2)
        s = set(word1) | set(word2)
        
        for i in s:
            if i in c1 and i in c2 and abs(c1[i] - c2[i]) > 3:
                return False
            if i not in c2 and c1[i] > 3: 
                return False
            if i not in c1 and c2[i] > 3:
                return False

        return True