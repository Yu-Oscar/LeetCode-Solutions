class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        l = 0
        while l < len(s):
            r = l
            while r < len(s) and s[l] == s[r]:
                r += 1

            if r - l >= 3:
                ans.append([l, r-1])

            l = r

        return ans
        