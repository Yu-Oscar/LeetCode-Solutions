class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            curr = i
            s_set = set()
            while curr < len(s):
                if s[curr] in s_set:
                    break
                s_set.add(s[curr])
                ans = max(ans, len(s_set))
                curr += 1

        return ans
            