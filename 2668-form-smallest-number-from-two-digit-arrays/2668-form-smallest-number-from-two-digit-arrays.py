class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        for num in nums1:
            if num in nums2:
                return num

        if nums1[0] < nums2[0]:
            return int(str(nums1[0])+str(nums2[0]))
        else:
            return int(str(nums2[0])+str(nums1[0]))