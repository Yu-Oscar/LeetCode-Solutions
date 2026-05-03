class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        d = {}
        most = 0
        ans = 0

        for right in range(len(s)):
            char = s[right]
            d[char] = d.get(char, 0) + 1
            most = max(most, d[char])

            if (right+1-left-most) > k:
                d[s[left]] -= 1
                left += 1
            
            ans = max(ans, right+1-left)

        return ans

            

        