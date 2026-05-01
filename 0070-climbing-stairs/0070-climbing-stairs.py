class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(left):
            if left == 0:
                return 1
            if left < 0:
                return 0

            if left in memo:
                return memo[left]

            memo[left] = dp(left - 1) + dp(left - 2)
            return memo[left]

        return dp(n)