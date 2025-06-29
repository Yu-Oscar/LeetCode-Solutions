class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:

        count_0 = 0
        count_1 = 0
        max_len = 0
        last_1 = False
        for d in s:
            if d == '0':
                if last_1:
                    max_len = max(max_len, 2 * min(count_0, count_1))
                    count_0 = 1
                    count_1 = 0
                    last_1 = False
                else:
                    count_0 += 1
            else:
                count_1 += 1
                last_1 = True
    

        return max(max_len, 2 * min(count_0, count_1))



        