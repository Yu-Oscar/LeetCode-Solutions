class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ans = ''
        for i in words:
            ans += i
            if ans == s:
                return True
        
        return False