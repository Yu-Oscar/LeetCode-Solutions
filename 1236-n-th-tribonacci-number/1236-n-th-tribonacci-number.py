class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def dp(k):
            if k == 0:
                return 0
            if k == 1 or k == 2:
                return 1
            if k in memo:
                return memo[k]
            
            memo[k] = dp(k-1) + dp(k-2) + dp(k-3)
            return memo[k]

        return dp(n)