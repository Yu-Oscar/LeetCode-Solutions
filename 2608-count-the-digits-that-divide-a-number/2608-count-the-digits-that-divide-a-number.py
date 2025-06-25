class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        for i in str(num):
            if num % int(i) == 0:
                ans += 1

        return ans