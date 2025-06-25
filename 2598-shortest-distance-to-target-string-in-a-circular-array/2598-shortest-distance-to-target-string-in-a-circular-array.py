class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        i = 0 
        n = len(words)
        while i <= n:
            if words[(startIndex + i) % n] == target or words[(startIndex - i) % n] == target:
                return i
            i += 1

        return -1
