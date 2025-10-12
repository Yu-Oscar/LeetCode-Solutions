class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1, s2, s3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        ans = []
        for word in words:
            w = set(list(word.lower()))
            if w <= s1 or w <= s2 or w <= s3:
                ans.append(word)

        return ans