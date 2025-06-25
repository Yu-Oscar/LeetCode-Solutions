class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        res = 0 
        prev = -1

        for i, fort in enumerate(forts):
            if fort != 0:
                if fort == -forts[prev] and prev != -1:
                    res = max(res, i - prev -1)
                prev = i
        return res

