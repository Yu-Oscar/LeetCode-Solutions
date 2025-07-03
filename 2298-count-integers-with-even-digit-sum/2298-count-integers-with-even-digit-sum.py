class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(2, num+1):
            
            temp = sum(int(d) for d in str(i))
            if temp % 2 == 0:
                ans += 1

        return ans


