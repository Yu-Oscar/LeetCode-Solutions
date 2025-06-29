class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        s = set()
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                s.add(i)
                s.add(int(num/i))
        
        return num == (sum(s) + 1)
        