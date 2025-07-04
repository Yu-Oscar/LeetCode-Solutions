class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        words = re.findall(r'\w+', paragraph.lower())
        banned_set = set(banned)

        # Count all words that are not banned
        word_counts = Counter(word for word in words if word not in banned_set)

        return word_counts.most_common(1)[0][0]