class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()

        for num in nums:
            for i in range(num[0], num[1] + 1):
                covered.add(i)

        print(covered)
        return len(covered)