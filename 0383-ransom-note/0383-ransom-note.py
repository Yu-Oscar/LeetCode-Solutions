class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        note, mag = Counter(list(ransomNote)), Counter(list(magazine))
        return note <= mag