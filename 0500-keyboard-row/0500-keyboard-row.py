class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            w = set(list(word.lower()))
            if w <= set("qwertyuiop") or w <= set("asdfghjkl") or w <= set("zxcvbnm"):
                ans.append(word)

        return ans