class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        smal = min(a,b)
        factors = set()

        for i in range(1, int(smal**0.5) + 1):
            if a % i == 0 and b % i == 0:
                factors.add(i)
            if a % (smal // i) == 0 and b % (smal // i) == 0:
                factors.add(smal // i)
        
        return len(factors)

        
            
        