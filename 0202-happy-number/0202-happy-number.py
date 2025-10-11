class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}
        while n not in visited:
            visited[n] = True
            ans = 0
            for d in str(n):
                ans += int(d)**2
            if ans == 1:
                return True
            n = ans
        return False
        