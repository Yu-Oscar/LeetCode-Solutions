class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(list(map(int, re.findall(r'\d+', word))))
)