class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        summ = sum(int(d) for d in str(x))
        if x % summ == 0:
            return summ
        else:
            return -1
        