class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i, word in enumerate(words):
            unique_set = set(word)
            for j in range(i + 1, len(words)):
                set2 = set(words[j])
                if unique_set == set2:
                    count += 1
        return count
        