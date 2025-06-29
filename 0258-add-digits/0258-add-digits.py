class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        while len(str(num)) != 1:
            ans = 0
            for d in str(num):
                ans += int(d)
            num = ans
        return num
        