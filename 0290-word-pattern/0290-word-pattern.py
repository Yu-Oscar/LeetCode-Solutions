class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pmapping, smapping = {}, {}
        pattern, s = list(pattern), s.split()
        if len(pattern) != len(s):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] in pmapping and pmapping[pattern[i]] != s[i]:
                return False
            if s[i] in smapping and smapping[s[i]] != pattern[i]:
                return False
    
            smapping[s[i]] = pattern[i]
            pmapping[pattern[i]] = s[i]
        return True
        