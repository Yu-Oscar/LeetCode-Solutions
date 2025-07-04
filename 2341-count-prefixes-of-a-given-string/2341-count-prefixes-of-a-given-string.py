class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        pre = ''
        ans = 0
        for c in s:
            pre += c
            for word in words:
                if pre == word:
                    ans += 1

        return ans
        