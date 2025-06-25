class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sen in sentences:
            ans = max(ans, len(sen.split()))
        return ans
        