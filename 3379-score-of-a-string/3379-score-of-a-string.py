class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        prev = s[0] 
        for c in s[0:]:
            score += abs(ord(c) - ord(prev))
            prev = c
        return score
        