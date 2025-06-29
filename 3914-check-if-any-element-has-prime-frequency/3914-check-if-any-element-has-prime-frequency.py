class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def isPrime(n: int) -> bool:
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
        from collections import Counter
        c = Counter(nums)
        for i in c:
            if isPrime(c[i]):
                return True
        
        return False