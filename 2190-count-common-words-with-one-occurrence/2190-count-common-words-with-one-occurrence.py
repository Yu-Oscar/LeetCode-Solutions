class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        c1 = Counter(words1)
        c2 = Counter(words2)
        
        ans = 0 
        for w in c1:
            if c1[w] == 1 and c2[w] == 1:
                ans += 1
        return ans