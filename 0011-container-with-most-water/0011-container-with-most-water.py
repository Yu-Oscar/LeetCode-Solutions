class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        ans = 0
        while left < right:
            vol = (right-left) * min(height[left], height[right])
            ans = max(ans, vol)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return ans
            