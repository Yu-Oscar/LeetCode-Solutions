class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        while len(word1) > 0 or len(word2) > 0:
            if len(word1) > 0:
                word3 += word1[0]
                word1 = word1[1:]
            if len(word2) > 0:
                word3 += word2[0]
                word2 = word2[1:]
        return word3