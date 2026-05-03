class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = left
        Set = set()
        ans = 0
        
        for right in range(len(s)):
            char = s[right]
            if char in Set:
                while char in Set:
                    Set.remove(s[left])
                    left += 1

            Set.add(char)
            ans = max(ans, right - left + 1)

        return ans

        return ans
            

