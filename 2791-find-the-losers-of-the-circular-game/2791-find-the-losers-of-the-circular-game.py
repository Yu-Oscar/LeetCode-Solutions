class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        ans = [0] * n
        ball = 0
        i = 0

        while max(ans) < 2:
            ball = (ball + i*k) % n
            ans[ball] += 1
            i += 1

        return [i+1 for i in range(len(ans)) if ans[i] == 0]
        