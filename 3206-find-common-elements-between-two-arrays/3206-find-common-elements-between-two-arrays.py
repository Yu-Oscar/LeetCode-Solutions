class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        ans = [0, 0]
        for i in c1:
            if c2[i]:
                ans[0] += c1[i]
        
        for i in c2:
            if c1[i]:
                ans[1] += c2[i]

        return ans